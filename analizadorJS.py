import ventana
import os

from errorLexico import ErrorLexico
from tokenLexico import Token

def obtenerContenidoJS(path):
    archivo = open(path,"r")

    ventana.obtenerPathSalidaLinux(archivo.readline(), archivo.readline())

    contenidoEntrada = ""
    for linea in archivo.readlines():
        contenidoEntrada += linea
    analizar(contenidoEntrada)

def analizar(contenido):
    dot = "digraph AFD{\nrankdir=LR\n"
    dot += "0 [label=\"S0\" shape=\"circle\"]\n"
    banderaComentarioIndividual = False
    banderaComentarioIndividual2 = False
    banderaComentarioMultilinea = False
    banderaComentarioMultilinea2 = False
    banderaDecimal = False
    banderaDecimal2 = False
    banderaEntero = False
    banderaIdentificador = False
    contenidoSalida = ""
    lexemaAuxiliar = ""
    dotAuxiliar = ""
    iteradorGrafo = 1
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
                dotAuxiliar = ""
                if banderaComentarioIndividual == False:
                    dotAuxiliar += str(iteradorGrafo)+" [label = \"S"+str(iteradorGrafo)+"\" shape = \"circle\"]\n"
                    dotAuxiliar += "0 -> "+str(iteradorGrafo)+" [label=\""+contenido[i]+"\"]\n"
                elif banderaComentarioMultilinea == False:
                    dotAuxiliar += str(iteradorGrafo)+" [label = \"S"+str(iteradorGrafo)+"\" shape = \"circle\"]\n"
                    dotAuxiliar += "0 -> "+str(iteradorGrafo)+" [label=\""+contenido[i]+"\"]\n"
            elif contenido[i] == "\n":
                estado = 0
                fila += 1
                columna = 0
                contenidoSalida += contenido[i]
                ventana.pintar("\n","otro")
            elif contenido[i].isalpha():
                estado = 5
                lexemaAuxiliar += contenido[i]
                dotAuxiliar = ""
                if banderaIdentificador == False:
                    dotAuxiliar += str(iteradorGrafo)+" [label = \"S"+str(iteradorGrafo)+"\" shape = \"doublecircle\"]\n"
                    dotAuxiliar += "0 -> "+str(iteradorGrafo)+" [label=\""+contenido[i]+"\"]\n"
            elif contenido[i] == "\t":
                estado = 0
                contenidoSalida += contenido[i]
                ventana.pintar("\t", "otro")
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
                dotAuxiliar = ""
                if banderaEntero == False or banderaDecimal == False:
                    if banderaDecimal == False:
                        dotAuxiliar += str(iteradorGrafo)+" [label = \"S"+str(iteradorGrafo)+"\" shape = \"circle\"]\n"
                        dotAuxiliar += "0 -> "+str(iteradorGrafo)+" [label=\""+contenido[i]+"\"]\n"
                    elif banderaEntero == False:
                        dotAuxiliar += str(iteradorGrafo)+" [label = \"S"+str(iteradorGrafo)+"\" shape = \"doublecircle\"]\n"
                        dotAuxiliar += "0 -> "+str(iteradorGrafo)+" [label = \""+contenido[i]+"\"]\n"
                lexemaAuxiliar += contenido[i]
            else:
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 1:
            if contenido[i] == "/":
                estado = 2
                lexemaAuxiliar += contenido[i]
                if banderaComentarioIndividual == False:
                    dotAuxiliar += str(iteradorGrafo+1)+" [label = \"S"+str(iteradorGrafo+1)+"\" shape = \"circle\"]\n"
                    dotAuxiliar += str(iteradorGrafo) + " -> "+str(iteradorGrafo+1)+" [label=\""+contenido[i]+"\"]\n"
                    iteradorGrafo += 1
            elif contenido[i] == "*":
                estado = 3
                lexemaAuxiliar += contenido[i]
                if banderaComentarioMultilinea == False:
                    dotAuxiliar += str(iteradorGrafo+1)+" [label = \"S"+str(iteradorGrafo+1)+"\" shape = \"circle\"]\n"
                    dotAuxiliar += str(iteradorGrafo) + " -> "+str(iteradorGrafo+1)+" [label=\""+contenido[i]+"\"]\n"
                    iteradorGrafo += 1
            else:
                dotAuxiliar = ""
                estado = 0
                i -= 1
                ventana.pintar("/","operador")
                contenidoSalida += lexemaAuxiliar
                lexemaAuxiliar = ""
        elif estado == 2:
            if contenido[i] == "\n":
                estado = 0
                lexemaAuxiliar += contenido[i]
                if banderaComentarioIndividual == False: 
                    dotAuxiliar += str(iteradorGrafo+1) + "[label = \"S"+str(iteradorGrafo+1)+"\" shape=\"doublecircle\"]\n"
                    dotAuxiliar += str(iteradorGrafo) + "-> " + str(iteradorGrafo+1) + "[label=\"Salto de linea\"]\n"
                    dot += dotAuxiliar
                    iteradorGrafo += 2
                    dotAuxiliar = ""
                    banderaComentarioIndividual = True
                dotAuxiliar = ""
                ventana.pintar(lexemaAuxiliar,"comentario")
                lexemaAuxiliar = ""
            else:
                if banderaComentarioIndividual2 == False:
                    dotAuxiliar += str(iteradorGrafo) + " -> "+str(iteradorGrafo)+" [label=\"Todo\"]\n"
                    banderaComentarioIndividual2 = True
                estado = 2
                lexemaAuxiliar += contenido[i]
        elif estado == 3:
            if contenido[i] == "*":
                estado = 4
                lexemaAuxiliar += contenido[i]
                if banderaComentarioMultilinea == False:
                    dotAuxiliar += str(iteradorGrafo+1) + " [label = \"S"+str(iteradorGrafo+1)+"\" shape=\"circle\"]\n"
                    dotAuxiliar += str(iteradorGrafo) + " -> " + str(iteradorGrafo+1) + "[label=\""+contenido[i]+"\"]\n"
                    iteradorGrafo += 1
            else:
                if banderaComentarioMultilinea2 == False:
                    dotAuxiliar += str(iteradorGrafo) + " -> "+str(iteradorGrafo)+" [label=\"Todo\"]\n"
                    banderaComentarioMultilinea2 = True
                estado = 3
                lexemaAuxiliar += contenido[i]
        elif estado == 4:
            if contenido[i] == "/":
                estado = 0
                lexemaAuxiliar += contenido[i]
                if banderaComentarioMultilinea == False:
                    dotAuxiliar += str(iteradorGrafo+1) + " [label = \"S"+str(iteradorGrafo+1)+"\" shape=\"doublecircle\"]\n"
                    dotAuxiliar += str(iteradorGrafo) + " -> " + str(iteradorGrafo+1) + "[label=\""+contenido[i]+"\"]\n"
                    dot += dotAuxiliar
                    iteradorGrafo += 2
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
                if banderaIdentificador == False:
                    dotAuxiliar += str(iteradorGrafo) + " -> " + str(iteradorGrafo) + " [label=\""+contenido[i]+"\"]\n"  
            else:
                if banderaIdentificador == False:
                    dot += dotAuxiliar
                    banderaIdentificador = True
                    iteradorGrafo += 1
                dotAuxiliar = ""
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
                if banderaEntero == False or banderaDecimal == False:
                    dotAuxiliar += str(iteradorGrafo) + " -> "+str(iteradorGrafo)+" [label=\""+contenido[i]+"\"]\n"
            elif contenido[i] == ".":
                estado = 8
                lexemaAuxiliar += contenido[i]
                if banderaDecimal == False:
                    dotAuxiliar += str(iteradorGrafo+1) + "[label=\"S"+str(iteradorGrafo+1)+"\" shape=\"circle\"]\n"
                    dotAuxiliar += str(iteradorGrafo)+" -> "+str(iteradorGrafo+1)+" [label=\"Punto\"]\n"
                    iteradorGrafo += 2
            else:
                estado = 0
                if banderaEntero == False:
                    dot += dotAuxiliar
                    banderaEntero = True
                    iteradorGrafo += 1
                ventana.pintar(lexemaAuxiliar,"intBoolean")
                contenidoSalida += lexemaAuxiliar
                lexemaAuxiliar = ""
                i -= 1
        elif estado == 8:
            if contenido[i].isdigit():
                estado = 8
                lexemaAuxiliar += contenido[i]
                if banderaDecimal == False:
                    if banderaDecimal2 == False:
                        dotAuxiliar += str(iteradorGrafo) + "[label=\"S"+str(iteradorGrafo)+"\" shape=\"doublecircle\"]\n"
                        dotAuxiliar += str(iteradorGrafo-1) + " -> " + str(iteradorGrafo) + "[label = \""+contenido[i]+"\"]"
                        banderaDecimal2 = True
                    else:
                        dotAuxiliar += str(iteradorGrafo) + " -> "+str(iteradorGrafo)+" [label=\""+contenido[i]+"\"]\n"
            else:
                estado = 0
                if lexemaAuxiliar[len(lexemaAuxiliar)-1].isdigit():
                    contenidoSalida += lexemaAuxiliar
                    if banderaDecimal == False:
                        dot += dotAuxiliar
                        banderaDecimal = True
                        iteradorGrafo += 1    
                    ventana.pintar(lexemaAuxiliar,"intBoolean")
                lexemaAuxiliar = ""
                i -= 1
        i += 1

    dot += "\"inicio\" [label=\"Inicio\" shape=\"plaintext\"]\n"
    dot += "\"inicio\" -> 0\n"
    dot += "}"

    graficoAFD(dot)
    ventana.reporteDeErroresTabla(listadoErrores, "/ErroresLexicosJS.html")
    ventana.guardarArchivoAnalizado(contenidoSalida)

def graficoAFD(entrada):
    #rutas de salida que almacenan el dot y la imagen a generar
    pathDot = ventana.obtenerDirectorioActual() + "/grafoJS.dot"
    pathImagen = ventana.obtenerDirectorioActual() + "/grafoJS.png"
    archivo = open(pathDot ,"w")
    archivo.write(entrada)
    archivo.close()

    #comando que realiza la compilacion del dot
    comando = "dot " + pathDot + " -Tpng -o " + pathImagen
    os.system(comando)
    ventana.abrirReporte(pathImagen)