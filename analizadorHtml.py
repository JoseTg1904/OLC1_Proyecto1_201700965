import platform

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
            pos = pos + 7
            pathSalida = path1[pos:len(path1)]
        else:
            aux = path2
            pos = aux.lower().find("pathl")
            pos = pos + 7
            pathSalida = path2[pos:len(path2)]
    elif platform.system() == "Windows":
        aux = path1 
        if aux.lower().find("pathw") != -1:
            pos = aux.lower().find("pathw")
            pos = pos + 7
            pathSalida = path1[pos:len(path1)]
        else:
            aux = path2
            pos = aux.lower().find("pathw")
            pos = pos + 7
            pathSalida = path2[pos:len(path2)]

    contenidoEntrada = ""
    for linea in archivo.readlines():
        contenidoEntrada += linea
    analizar(contenidoEntrada)

def analizar(contenido):
    contenidoSalida = ""
    fila = 0
    columna = 0
    estado = 0
    ignorar = False
    enlace = False

    for i in range(len(contenido)):
        columna += 1
        if ignorar == False:
            if estado is 0:
                if contenido[i] == "\n":
                    columna = 0
                    fila += 1
                    estado = 0
                    contenidoSalida += contenido[i]
                if contenido[i] == "<":
                    estado = 1
                    contenidoSalida += contenido[i]
            elif estado is 1:
                if contenido[i].lower() == "h":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i] == "/":
                    estado = 1
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "t":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "b":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "p":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i].lower() == "i":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "a":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "u":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "o":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "l":
                    estado = 2
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "c":
                    estado = 10
                    contenidoSalida += contenido[i]
            elif estado is 2:
                if contenido[i].lower() == "t":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "e":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "i":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "o":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i] == "1":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i] == "2":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i] == "3":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i] == "4":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i] == "5":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i] == "6":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i] == "r":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i].lower() == "m":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i] == " ":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i] == ">":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "l":
                    estado = 5
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "h":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i].lower() == "d":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i].lower() == "a":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "f":
                    estado = 3
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "b":
                    estado = 3
                    contenidoSalida += contenido[i]
            elif estado is 3:
                if contenido[i].lower() == "m":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "a":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "t":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "d":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "g":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "h":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "p":
                    estado = 4
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "o":
                    estado = 4
                    contenidoSalida += contenido[i]
            elif estado is 4:
                if contenido[i].lower() == "l":
                    estado = 5
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "d":
                    estado = 5
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "y":
                    estado = 5
                    contenidoSalida += contenido[i] 
                    ignorar = True
                elif contenido[i].lower() == " ":
                    estado = 5
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "r":
                    estado = 6
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "t":
                    estado = 5
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "o":
                    estado = 5
                    contenidoSalida += contenido[i]
            elif estado is 5:
                if contenido[i] == ">":
                    estado = 0
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "e":
                    estado = 5
                    contenidoSalida += contenido[i]
                    ignorar = True
                elif contenido[i].lower() == "s":
                    estado = 6
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "i":
                    estado = 6
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "t":
                    estado = 5
                    ignorar = True
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "y":
                    estado = 10
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "a":
                    estado = 6
                    contenidoSalida += contenido[i]
            elif estado is 6:
                if contenido[i].lower() == "r":
                    estado = 7
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "e":
                    estado = 7
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "o":
                    estado = 7
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "d":
                    estado = 5
                    ignorar = True
                    contenidoSalida += contenido[i]
            elif estado is 7:
                if contenido[i].lower() == "c":
                    estado = 8
                    contenidoSalida += contenido[i]
                elif contenido[i].lower() == "f":
                    estado = 8
                    contenidoSalida += contenido[i]
                    enlace = True
                elif contenido[i].lower() == "n":
                    estado = 5
                    ignorar = True
                    contenidoSalida += contenido[i]
            elif estado is 8:
                if contenido[i] == "=":
                    estado = 9
                    contenidoSalida += contenido[i]
            elif estado is 9:
                if contenido[i] == "\"" or contenido[i] == "\'":
                    estado = 10
                    contenidoSalida += contenido[i]
                    ignorar = True
            elif estado is 10:
                if contenido[i] == "\"" or contenido[i] == "\'":
                    estado = 5
                    contenidoSalida += contenido[i]
                    if enlace is True:
                        ignorar = True
                elif contenido[i].lower() == "i":
                    estado = 5
                    ignorar = True
                    contenidoSalida += contenido[i]
        else:
            if contenido[i+1] == "<":
                ignorar = False
                enlace = False
                estado = 0
            if contenido[i+1] == "\"" or contenido[i+1] == "\'":
                ignorar = False
                estado = 10
            contenidoSalida += contenido[i]

    print(contenidoSalida)
    print("simon si sali")
