import platform

from errorLexico import ErrorLexico
from token import Token

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
    analizar(contenidoEntrada, pathSalida)

def analizar(contenido, path):
    contenidoSalida = ""
    lexemaAuxiliar = ""
    recorrido = ""
    fila = 0
    columna = 0
    estado = 0
    listadoErrores = []
    listadoTokens = []

    i = 0
    while i < len(contenido):
        columna += 1
        if estado == 0:
            if contenido[i] == "\n":
                estado = 0
                fila += 1
                columna = 0
                contenidoSalida += contenido[i]
            elif contenido[i] == "/":
                estado = 1
            elif contenido[i] == "{":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_llaveA","0"))
            elif contenido[i] == "}":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_llaveC","0"))
            elif contenido[i] == "*":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_asterisco","0"))
            elif contenido[i] == " ":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_espacio","0"))
            elif contenido[i] == ";":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_puntoYComa","0"))
            elif contenido[i].isalpha() or contenido[i] == "-":
                estado = 4
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == "#":
                estado = 4
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_numeral","0"))
            elif contenido[i].isalpha() or contenido[i] == "-":
                estado = 4
                lexemaAuxiliar += contenido[i]
                recorrido += "0, "
            elif contenido[i] == ".":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_punto","0"))
            elif contenido[i] == ":":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_dosPuntos","0"))
            elif contenido[i].isdigit():
                estado = 5
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == "(":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_parentesisA","0"))
            elif contenido[i] == ")":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_parentesisC","0"))
            elif contenido[i] == "%":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_porcentaje","0"))
            elif contenido[i] == "\"":
                estado = 7
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_comillas","0"))
            else:
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 1:
            if contenido[i] == "*":
                estado = 2
            else:
                estado = 1
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 2:
            if contenido[i] == "*":
                estado = 3
            else:
                estado = 2
        elif estado == 3:
            if contenido[i] == "/":
                estado = 0
            else:
                estado = 3
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 4:
            if contenido[i] == "-" or contenido[i].isalpha() or contenido[i].isdigit():
                lexemaAuxiliar += contenido[i]
                estado = 4
                recorrido += "4, "
            else:
                if lexemaAuxiliar.lower() == "color":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_color",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "border":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_border",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "text-align":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_textAlign",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-weight":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_fontWeight",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-left":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_paddingLeft",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-top":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_paddingTop",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "line-height":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_lineHeight",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-top":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_marginTop",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-left":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_marginLeft",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "display":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_display",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "top":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_top",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "float":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_float",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "min-width":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_minWidth",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "background-color":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_backgroundColor",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "opacity":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_opacity",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-family":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_fontFamily",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-size":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_fontSize",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-right":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_paddingRight",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_padding",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "width":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_width",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-right":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_marginRight",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_margin",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "position":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_position",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "right":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_right",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "clear":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_clear",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "max-height":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_maxHeight",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "background-image":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_backgroundImage",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "background":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_background",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-style":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_fontStyle",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_font",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-bottom":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_paddingBottom",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "height":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_height",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-bottom":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_marginBottom",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "border-style":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_borderStyle",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "bottom":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_bottom",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "left":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_left",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "max-width":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_maxWidth",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "min-height":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_minHeight",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "px":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_px",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "em":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_em",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "vh":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_vh",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "vw":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_vw",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "in":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_in",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "cm":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_cm",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "mm":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_mm",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "pt":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_pt",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "pc":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_pc",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "content":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_content",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "url":
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_url",recorrido+"4"))
                    recorrido = ""
                    i -= 1
                else:
                    contenidoSalida += lexemaAuxiliar
                    lexemaAuxiliar = ""
                    estado = 0
                    listadoTokens.append(Token("tk_id",recorrido))
                    recorrido = ""
                    i -= 1
        elif estado == 5:
            if contenido[i].isdigit():
                lexemaAuxiliar += contenido[i]
                estado = 5
                recorrido += "5, "
            elif contenido[i] == ".":
                estado = 6
                recorrido += "5, "
                lexemaAuxiliar += contenido[i]
            else:
                listadoTokens.append(Token("tk_numero", recorrido+"5"))
                contenidoSalida += lexemaAuxiliar
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
        elif estado == 6:
            if contenido[i].isdigit():
                estado = 6
                lexemaAuxiliar += contenido[i]
                recorrido += "6, "
            else:
                listadoTokens.append(Token("tk_numeroDecimal", recorrido+"5"))
                contenidoSalida += lexemaAuxiliar
                lexemaAuxiliar = ""
                estado = 0
                i -= 1
        elif estado == 7:
            if contenido[i] == "\"":
                estado = 0
                contenidoSalida += lexemaAuxiliar
                contenidoSalida += contenido[i]
                lexemaAuxiliar = ""
                listadoTokens.append(Token("tk_comillas","0"))
            else:
                estado = 7
                lexemaAuxiliar += contenido[i]
        i += 1

    reporteErrores(listadoErrores)
    generarArchivoSalida(contenidoSalida, path)


def generarArchivoSalida(contenido, path):
    archivo = open(path,"w")
    archivo.write(contenido)

def reporteErrores(errores):
    archivo = open("/home/jose/Escritorio/ErroresLexicosHTML.html","w")
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