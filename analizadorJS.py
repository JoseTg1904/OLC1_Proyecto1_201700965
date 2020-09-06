import ventana
import os

from errorLexico import ErrorLexico
from tokenLexico import Token

def obtenerContenidoJS(path):
    archivo = open(path,"r")

    path1 = archivo.readline()
    path2 = archivo.readline()
    
    aux = path1 
    if aux.lower().find("pathl") != -1:
        pos = aux.lower().find("pathl")
        pos = pos + 6
        pathSalida = path1[pos:len(path1)]
    else:
        aux = path2
        pos = aux.lower().find("pathl")
        pos = pos + 6
        pathSalida = path2[pos:len(path2)]

    pathSalida = pathSalida.strip(" ")

    contenidoEntrada = ""
    for linea in archivo.readlines():
        contenidoEntrada += linea
    analizar(contenidoEntrada, pathSalida)

def analizar(contenido, path):
    dot = "digraph AFD{\nrankdir=LR\n"
    banderaComentarioIndividual = False
    banderaComentarioMultilinea = False
    banderaDecimal = False
    banderaEntero = False
    contenidoSalida = ""
    lexemaAuxiliar = ""
    fila = 0
    columna = 0
    estado = 0
    listadoErrores = []

    i = 0
    while i < len(contenido):
        columna += 1
        if estado == 0:
            if contenido[i] == "/":
                estado = 1
                lexemaAuxiliar = contenido[i]
            elif contenido[i] == "\n":
                estado = 0
                fila += 1
                columna = 0
                contenidoSalida += contenido[i]
                ventana.pintar("\n","otro")
            elif contenido[i].isalpha():
                estado = 5
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == "=":
                estado = 0
                ventana.pintar("=","operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == " ":
                estado = 0
                ventana.pintar(" ","otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == "\"" or contenido[i] == "“" or contenido[i] == "\'" or contenido[i] == "‘":
                estado = 6
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == "*":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == "(":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == ")":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == "}":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == "{":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == ";":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == "<":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == ">":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == "+":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == "-":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == ",":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i] == "!":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == "&":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == "|":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == ".":
                estado = 0 
                ventana.pintar(contenido[i],"operador")
                contenidoSalida += contenido[i]
            elif contenido[i] == ":":
                estado = 0 
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
            elif contenido[i].isdigit():
                estado = 7
                lexemaAuxiliar += contenido[i]
            else:
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 1:
            if contenido[i] == "/":
                estado = 2
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == "*":
                estado = 3
                lexemaAuxiliar += contenido[i]
            else:
                estado = 0
                i -= 1
                ventana.pintar("/","operador")
                lexemaAuxiliar = ""
        elif estado == 2:
            if contenido[i] == "\n":
                estado = 0
                lexemaAuxiliar += contenido[i]
                if banderaComentarioIndividual == False:
                    dot += "0 [label=\"S0\" shape=\"circle\"]\n"
                    dot += "1 [label=\"S1\" shape=\"circle\"]\n"
                    dot += "2 [label=\"S2\" shape=\"circle\"]\n"
                    dot += "3 [label=\"S3\" shape=\"doublecircle\"]\n"
                    dot += "0 -> 1 [label=\"/\"]"
                    dot += "1 -> 2 [label=\"/\"]"
                    dot += "2 -> 2 [label=\"Todo\"]"
                    dot += "2 -> 3 [label=\"Salto de linea\"]"
                    banderaComentarioIndividual = True
                ventana.pintar(lexemaAuxiliar,"comentario")
                lexemaAuxiliar = ""
            else:
                estado = 2
                lexemaAuxiliar += contenido[i]
        elif estado == 3:
            if contenido[i] == "*":
                estado = 4
                lexemaAuxiliar += contenido[i]
            else:
                estado = 3
                lexemaAuxiliar += contenido[i]
        elif estado == 4:
            if contenido[i] == "/":
                estado = 0
                lexemaAuxiliar += contenido[i]
                if banderaComentarioMultilinea == False:
                    dot += "5 [label=\"S1\" shape=\"circle\"]\n"
                    dot += "6 [label=\"S4\" shape=\"circle\"]\n"
                    dot += "7 [label=\"S5\" shape=\"circle\"]\n"
                    dot += "8 [label=\"S6\" shape=\"doublecircle\"]\n"
                    dot += "0 -> 5 [label=\"/\"]"
                    dot += "5 -> 6 [label=\"*\"]"
                    dot += "6 -> 6 [label=\"Todo\"]"
                    dot += "6 -> 7 [label=\"*\"]"
                    dot += "7 -> 8 [label=\"/\"]"
                    banderaComentarioMultilinea = True
                ventana.pintar(lexemaAuxiliar,"comentario")
                lexemaAuxiliar = ""
            else:
                estado = 3
                i -= 1
        elif estado == 5:
            if contenido[i].isalpha() or contenido[i].isdigit() or contenido[i] == "_":
                lexemaAuxiliar += contenido[i]
                estado = 5
            else:
                if lexemaAuxiliar.lower() == "var":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "true":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"intBoolean")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "false":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"intBoolean")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "if":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "else":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "console":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "log":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "for":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "while":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "do":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "continue":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "break":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "return":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "function":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "constructor":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "class":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "this":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "math":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                elif lexemaAuxiliar.lower() == "pow":
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                else:
                    estado = 0
                    i -= 1
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"variable")
                    lexemaAuxiliar = ""
        elif estado == 6:
            if contenido[i] == "\"" or contenido[i] == "“" or contenido[i] == "\'" or contenido[i] == "‘":
                estado = 0
                ventana.pintar(lexemaAuxiliar,"stringChar")
                ventana.pintar(contenido[i],"otro")
                lexemaAuxiliar += contenido[i]
                contenidoSalida += lexemaAuxiliar
                lexemaAuxiliar = ""
            else:
                lexemaAuxiliar += contenido[i]
                estado = 6
        elif estado == 7:
            if contenido[i].isdigit():
                estado = 7
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == ".":
                estado = 8
                lexemaAuxiliar += contenido[i]
            else:
                estado = 0
                if banderaEntero == False:
                    dot += "13 [label=\"S7\" shape=\"doublecircle\"]\n"
                    dot += "0 -> 13 [label=\"Numero\"]"
                    dot += "13 -> 13 [label=\"Numero\"]"
                    banderaEntero = True
                ventana.pintar(lexemaAuxiliar,"intBoolean")
                lexemaAuxiliar = ""
                i -= 1
        elif estado == 8:
            if contenido[i].isdigit():
                estado = 8
                lexemaAuxiliar += contenido[i]
            else:
                estado = 0
                if banderaDecimal == False:
                    dot += "10 [label=\"S7\" shape=\"circle\"]\n"
                    dot += "11 [label=\"S8\" shape=\"doublecircle\"]\n"
                    dot += "0 -> 10 [label=\"Numero\"]"
                    dot += "10 -> 10 [label=\"Numero\"]"
                    dot += "10 -> 11 [label=\"Punto\"]"
                    dot += "11 -> 11 [label=\"Numero\"]"
                    banderaDecimal = True
                ventana.pintar(lexemaAuxiliar,"intBoolean")
                lexemaAuxiliar = ""
                i -= 1
        i += 1

    dot += "15 [label=\"Inicio\" shape=\"plaintext\"]\n"
    dot += "15 -> 0"
    dot += "}"
    graficoAFD(dot)
    reporteErrores(listadoErrores)
    generarArchivoSalida(contenidoSalida, path)

def graficoAFD(entrada):
    pathDot = ventana.obtenerDirectorioActual() + "/grafoJS.dot"
    pathImagen = ventana.obtenerDirectorioActual() + "/grafoJS.png"
    archivo = open(pathDot ,"w")
    archivo.write(entrada)
    archivo.close()
    comando = "dot " + pathDot + " -Tpng -o " + pathImagen
    os.system(comando)
    ventana.abrirReporte(pathImagen)

def generarArchivoSalida(contenido, path):
    archivo = open(path,"w")
    archivo.write(contenido)

def reporteErrores(errores):
    pathSalida = ventana.obtenerDirectorioActual() + "/ErroresLexicosJS.html"
    archivo = open(pathSalida,"w")
    contenidoErrores = """<html>
    <table class=\"egt\" border>
    <tr>
        <th> No. </th>
        <th> Linea </th>
        <th> Columna </th>
        <th> Descripcion </th>
    </tr>"""

    iterador = 1

    for error in errores:
        contenidoErrores += "<tr>"
        contenidoErrores += "<td> " + str(iterador) + " </td>"
        contenidoErrores += "<td> " + str(error.fila) +" </td>"
        contenidoErrores += "<td> " + str(error.columna) + " </td>"
        contenidoErrores += "<td> El caracter " + error.error + " no pertenece al lenguaje </td>"
        contenidoErrores += "</tr>"
        iterador += 1

    contenidoErrores += """</table>
    </html>"""
    archivo.write(contenidoErrores)
    archivo.close()
    ventana.abrirReporte(pathSalida)