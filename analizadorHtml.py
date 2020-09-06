from errorLexico import ErrorLexico

import ventana

def obtenerContenido(path):
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
            if contenido[i] == "\n":
                estado = 0
                fila += 1
                columna = 0
                contenidoSalida += contenido[i]
                ventana.pintar("\n","otro")
            elif contenido[i] == "<":
                estado = 0
                contenidoSalida += contenido[i]
                ventana.pintar("<","operador")
            elif contenido[i] == ">":
                contenidoSalida += contenido[i]
                lexemaAuxiliar = ""
                estado = 3
                ventana.pintar(">","operador")
            elif contenido[i] == "=":
                estado = 0
                contenidoSalida += contenido[i]
                ventana.pintar("=","operador")
            elif contenido[i] == "/":
                estado = 0
                contenidoSalida += contenido[i]
                ventana.pintar("/","otro")
            elif contenido[i] == " ":
                estado = 0
                contenidoSalida += contenido[i]
                ventana.pintar(" ","otro")
            elif contenido[i] == "\"" or contenido[i] == "\'" or contenido[i] == "‘" or contenido[i] == "“":
                estado = 4
                ventana.pintar(contenido[i],"otro")
                contenidoSalida += contenido[i]
                lexemaAuxiliar = ""
            elif contenido[i].isalpha():
                estado = 1
                lexemaAuxiliar += contenido[i]
            else:
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 1:   
            if contenido[i].isalpha():
                estado = 1
                lexemaAuxiliar += contenido[i]
            elif contenido[i].isdigit():
                estado = 2
                lexemaAuxiliar += contenido[i]
            else: 
                if lexemaAuxiliar.lower() == "html":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0 
                    i -= 1
                elif lexemaAuxiliar.lower() == "head":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "title":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "body":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "p":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "img":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "src":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "a":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "href":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "ul":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "li":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "style":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "table":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "th":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "tr":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "td":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "caption":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "colgroup":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "col":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "thead":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "tbody":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                elif lexemaAuxiliar.lower() == "tfoot":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
                else:
                    lexemaAuxiliar = ""
                    estado = 0
                    i -= 1
        elif estado == 2:
            if lexemaAuxiliar.lower() == "h1":
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"reservada")
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
            elif lexemaAuxiliar.lower() == "h2":
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"reservada")
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
            elif lexemaAuxiliar.lower() == "h3":
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"reservada")
                lexemaAuxiliar = ""
                estado = 0
                i -= 1    
            elif lexemaAuxiliar.lower() == "h4":
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"reservada")
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
            elif lexemaAuxiliar.lower() == "h5":
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"reservada")
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
            elif lexemaAuxiliar.lower() == "h6":
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"reservada")
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
            else:
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
        elif estado == 3:
            if contenido[i] == "<":
                estado = 0
                i -= 1
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"entreEtiquetas")
                lexemaAuxiliar = ""
            else:
                estado = 3
                lexemaAuxiliar += contenido[i]
        elif estado == 4:
            if contenido[i] == "\"" or contenido[i] == "\'":
                estado = 0
                contenidoSalida += lexemaAuxiliar
                contenidoSalida += contenido[i]
                ventana.pintar(lexemaAuxiliar,"otro")
                ventana.pintar(contenido[i],"otro")
                lexemaAuxiliar = ""
            else:
                estado = 4
                lexemaAuxiliar += contenido[i]
        i += 1

    reporteErrores(listadoErrores)
    generarArchivoSalida(contenidoSalida, path)

def generarArchivoSalida(contenido, path):
    archivo = open(path,"w")
    archivo.write(contenido)

def reporteErrores(errores):
    pathSalida = ventana.obtenerDirectorioActual() + "/ErroresLexicosHTML.html"
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