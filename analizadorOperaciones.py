from tokenLexico import TokenParea

def obtenerContenidoOperaciones(path):
    archivo = open(path,"r")
    contenidoEntrada = ""
    for linea in archivo.readlines():
        contenidoEntrada += linea
    analizarLexico(contenidoEntrada)

def analizarLexico(contenido):
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
                else:
                    listadoTokens.append(TokenParea("tk_ID", lexemaAuxiliar, 8))
                    i -= 1
                    lexemaAuxiliar = ""
                    estado = 0
            i += 1
        i = 0
        estado = 0
        lexemaAuxiliar = ""
        #mandar al analisis sintactico
        for a in listadoTokens:
            print(a.tipo+" "+a.valor+" "+str(a.idP))
        listadoTokens.clear()
        for a in listadoTokens:
            print(a.tipo+" "+a.valor+" "+str(a.idP))