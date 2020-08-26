import platform
import re

from errorLexico import ErrorLexico

pathSalida = ""
fila = 0
columna = 0
listadoErrores = []
estado = 0
contenidoEntrada = ""
contenidoSalida = ""
ignorar = False

def obtenerContenido(path):
    archivo = open(path,"r")

    path1 = archivo.readline()
    path2 = archivo.readline()
    

    if platform.system() == "Linux":
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
    elif platform.system() == "Windows":
        aux = path1 
        if aux.lower().find("pathw") != -1:
            pos = aux.lower().find("pathw")
            pos = pos + 6
            pathSalida = path1[pos:len(path1)]
        else:
            aux = path2
            pos = aux.lower().find("pathw")
            pos = pos + 6
            pathSalida = path2[pos:len(path2)]

    pathSalida = pathSalida.strip(" ")

    contenidoEntrada = ""
    for linea in archivo.readlines():
        contenidoEntrada += linea
    analizar(contenidoEntrada)

def analizar(contenido):
    contenidoSalida = ""
    lexema = ""
    fila = 0
    columna = 0
    estado = 0
    ignorar = False

    for i in range(len(contenido)):
        columna += 1
        if ignorar == False:
            if estado is 0:
                if contenido[i] == "\n":
                    estado = 0
                    fila += 1
                    columna = 0
                    contenidoSalida += contenido[i]
                elif contenido[i] == "<":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i] == ">":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i] == "=":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i] == "/":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i] == " ":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i] == "\"" or contenido[i] == "\'":
                    #parte a los identificadores que van contenidos 
                    pass
        else:
            pass

    print(contenidoSalida)