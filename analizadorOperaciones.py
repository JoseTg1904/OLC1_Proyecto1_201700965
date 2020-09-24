from tokenLexico import TokenParea, ResultadoSintactico
import ventana

indiceParea = 0
contadorParentesis = 0
tokenPareaActual = TokenParea("", "", 0)
estadoOperacion = True
listadoTokens = []

def obtenerContenidoOperaciones(path):
    archivo = open(path,"r")
    contenidoEntrada = ""
    for linea in archivo.readlines():
        contenidoEntrada += linea
    analizarLexico(contenidoEntrada)

def analizarLexico(contenido):
    global listadoTokens, indiceParea, estadoOperacion, contadorParentesis
    resultados = []

    sinSaltos = contenido.split("\n")
    for j in range(0, len(sinSaltos)-1):
        i = 0
        lexemaAuxiliar = ""
        estado = 0
        listadoTokens = []
        operacion = sinSaltos[j]
        operacion = operacion.replace(" ","")
        operacion = operacion.replace("\t","")
        while i < len(operacion):
            if estado == 0:
                if operacion[i] == "(":
                    estado = 0
                    listadoTokens.append(TokenParea("tk_ParA", "(", 0))
                elif operacion[i] == ")":
                    estado = 0
                    listadoTokens.append(TokenParea("tk_ParC", ")", 1))
                elif operacion[i] == "+":
                    estado = 0
                    listadoTokens.append(TokenParea("tk_Mas", "+", 2))
                elif operacion[i] == "-":
                    estado = 0
                    listadoTokens.append(TokenParea("tk_Menos", "-", 3))
                elif operacion[i] == "*":
                    estado = 0
                    listadoTokens.append(TokenParea("tk_Asterisco", "*", 4))
                elif operacion[i] == "/":
                    estado = 0
                    listadoTokens.append(TokenParea("tk_Diagonal", "/", 5))
                elif operacion[i].isdigit():
                    estado = 1
                    lexemaAuxiliar += operacion[i]
                elif operacion[i].isalpha():
                    estado = 3
                    lexemaAuxiliar += operacion[i]
            elif estado == 1:
                if operacion[i].isdigit():
                    estado = 1
                    lexemaAuxiliar += operacion[i]
                    if i == len(operacion)-1:
                        if lexemaAuxiliar[len(lexemaAuxiliar)-1].isdigit():
                            listadoTokens.append(TokenParea("tk_NumeroEntero", lexemaAuxiliar, 6))
                            lexemaAuxiliar = ""
                            estado = 0        
                elif operacion[i] == ".":
                    estado = 2
                    lexemaAuxiliar += operacion[i]
                else:
                    listadoTokens.append(TokenParea("tk_NumeroEntero", lexemaAuxiliar, 6))
                    i -= 1
                    lexemaAuxiliar = ""
                    estado = 0
            elif estado == 2:
                if operacion[i].isdigit():
                    lexemaAuxiliar += operacion[i]
                    estado = 2
                    if i == len(operacion)-1:
                        if lexemaAuxiliar[len(lexemaAuxiliar)-1].isdigit():
                            listadoTokens.append(TokenParea("tk_NumeroDecimal", lexemaAuxiliar, 7))
                            lexemaAuxiliar = ""
                            estado = 0    
                else:
                    if lexemaAuxiliar[len(lexemaAuxiliar)-1].isdigit():
                        listadoTokens.append(TokenParea("tk_NumeroDecimal", lexemaAuxiliar, 7))
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
            elif estado == 3:
                if operacion[i].isdigit() or operacion[i].isalpha():
                    lexemaAuxiliar += operacion[i]
                    estado = 3
                    if i == len(operacion)-1:
                        if lexemaAuxiliar[len(lexemaAuxiliar)-1].isdigit() or lexemaAuxiliar[len(lexemaAuxiliar)-1].isalpha() :
                            listadoTokens.append(TokenParea("tk_ID", lexemaAuxiliar, 8))
                            lexemaAuxiliar = ""
                            estado = 0    
                else:
                    listadoTokens.append(TokenParea("tk_ID", lexemaAuxiliar, 8))
                    i -= 1
                    lexemaAuxiliar = ""
                    estado = 0
            i += 1

        if len(listadoTokens) > 0:
            print(sinSaltos[j])
            analizadorSintactico()
            print("indice", indiceParea, "longitud listado", len(listadoTokens))
            if indiceParea != len(listadoTokens):
                estadoOperacion = False
            resultados.append(ResultadoSintactico(sinSaltos[j], estadoOperacion))
    
    reporteSintactico(resultados)

def reporteSintactico(listaResultados):
    pathSalida = ventana.obtenerDirectorioActual() + "/Operaciones.html"
    archivo = open(pathSalida,"w")
    contenidoErrores = """<html>
    <table class=\"egt\" border>
    <tr>
        <th> No. </th>
        <th> Operacion </th>
        <th> Resultado </th>
    </tr>"""

    iterador = 1

    for error in listaResultados:
        contenidoErrores += "<tr>"
        contenidoErrores += "<td> " + str(iterador) + " </td>"
        contenidoErrores += "<td> " + str(error.operacion) +" </td>"
        contenidoErrores += "<td> " + str(error.resultado) + " </td>"
        contenidoErrores += "</tr>"
        iterador += 1

    contenidoErrores += """</table>
    </html>"""
    archivo.write(contenidoErrores)
    archivo.close()
    ventana.abrirReporte(pathSalida)

#metodo inicial que llama a la produccion inicial de la gramatica
def analizadorSintactico():
    """
    gramatica para operaciones aritmeticas basicas, ya sin recursividad por la izquierda
    A -> B A'
    A' -> + B A' | - B A' | EPSILON
    B -> C B'
    B' -> * C B' | / C B' | EPSILON
    C -> (A) | ID | NUMERO | NUMERODECIMAL
    """
    global listadoTokens, tokenPareaActual, indiceParea, estadoOperacion
    indiceParea = 0
    estadoOperacion = True
    tokenPareaActual = listadoTokens[0]
    prodA()

#metodos recursivos que simulan las producciones de la gramatica
def prodA():
    print("produccion A")
    if tokenPareaActual != None:
        prodB()
        prodAP()

def prodAP():
    print("produccion AP")
    if tokenPareaActual != None:
        if tokenPareaActual.idP == 2:
            validacionParea(2)
            prodB()
            prodAP()
        #signo menos
        elif tokenPareaActual.idP == 3:
            validacionParea(3)
            prodB()
            prodAP()

def prodB():
    print("produccion B")
    if tokenPareaActual != None:
        prodC()
        prodBP()

def prodBP():
    print("produccion BP")

    if tokenPareaActual != None:
        #signo por
        if tokenPareaActual.idP == 4:
            validacionParea(4)
            prodC()
            prodBP()
        #signo division
        elif tokenPareaActual.idP == 5:
            validacionParea(5)
            prodC()
            prodBP()

def prodC():
    print("produccion C")
    if tokenPareaActual != None:
        if tokenPareaActual.idP == 0:
            #parentesis que abre
            validacionParea(0)
            prodA()
            #parentesis que cierra
            validacionParea(1)
            #numero entero
        elif tokenPareaActual.idP == 6:
            validacionParea(6)
        #numero decimal
        elif tokenPareaActual.idP == 7:
            validacionParea(7)
        #identificador
        elif tokenPareaActual.idP == 8:
            validacionParea(8)
        #error
        else:
            validacionParea(-1)

#metodo de parea, el cual realiza la validacion del terminal que proviene de los metodos recursivos
def validacionParea(idParea):
    global tokenPareaActual, indiceParea, estadoOperacion, listadoTokens, contadorParentesis
    
    if tokenPareaActual != None:
        print("produccion Parea ", tokenPareaActual.valor, tokenPareaActual.idP,"pre analisis",idParea)
        if idParea != tokenPareaActual.idP:
            estadoOperacion = False
            tokenPareaActual = None
        else:
            indiceParea += 1
            if indiceParea < len(listadoTokens):
                tokenPareaActual = listadoTokens[indiceParea]
            else:
                tokenPareaActual = None
