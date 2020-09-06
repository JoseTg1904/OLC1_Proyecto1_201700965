import ventana

from errorLexico import ErrorLexico
from tokenLexico import Token

def obtenerContenidoCSS(path):
    archivo = open(path,"r")

    ventana.obtenerPathSalidaLinux(archivo.readline(), archivo.readline())

    pathSalida = ""
    
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
                ventana.pintar("\n","otro")
                listadoTokens.append(Token("tk_saltoLinea","0"," "))
            elif contenido[i] == "/":
                estado = 1
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == "{":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_llaveA","0",contenido[i] ))
                ventana.pintar("{","otro")
            elif contenido[i] == "}":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_llaveC","0",contenido[i]))
                ventana.pintar("}","otro")
            elif contenido[i] == "*":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_asterisco","0",contenido[i]))
                ventana.pintar("*","operador")
            elif contenido[i] == " ":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_espacio","0",contenido[i]))
                ventana.pintar(" ","otro")
            elif contenido[i] == ";":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_puntoYComa","0",contenido[i]))
                ventana.pintar(";","otro")
            elif contenido[i] == ",":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_coma","0",contenido[i]))
                ventana.pintar(",","otro")
            elif contenido[i].isalpha() or contenido[i] == "-":
                estado = 4
                lexemaAuxiliar += contenido[i]
                recorrido = "0, "
            elif contenido[i] == "#":
                estado = 4
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_numeral","0",contenido[i]))
                ventana.pintar("#","operador")
            elif contenido[i] == ".":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_punto","0",contenido[i]))
                ventana.pintar(".","operador")
            elif contenido[i] == ":":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_dosPuntos","0",contenido[i]))
                ventana.pintar(":","operador")
            elif contenido[i].isdigit():
                estado = 5
                recorrido += "0, "
                lexemaAuxiliar += contenido[i]
            elif contenido[i] == "(":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_parentesisA","0",contenido[i]))
                ventana.pintar("(","otro")
            elif contenido[i] == ")":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_parentesisC","0",contenido[i]))
                ventana.pintar(")","otro")
            elif contenido[i] == "%":
                estado = 0
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_porcentaje","0",contenido[i]))
                ventana.pintar("%","operador")
            elif contenido[i] == "\"" or contenido[i] == "“":
                estado = 7
                contenidoSalida += contenido[i]
                listadoTokens.append(Token("tk_comillas","0",contenido[i]))
                ventana.pintar("\"","otro")
            else:
                listadoErrores.append(ErrorLexico(contenido[i],fila,columna))
        elif estado == 1:
            if contenido[i] == "*":
                estado = 2
                lexemaAuxiliar += contenido[i]
            else:                
                estado = 0
                listadoErrores.append(ErrorLexico("/",fila,columna-1))
                lexemaAuxiliar = ""
                i -= 1
        elif estado == 2:
            if contenido[i] == "*":
                estado = 3
                lexemaAuxiliar += contenido[i]
            else:
                lexemaAuxiliar += contenido[i]
                estado = 2
        elif estado == 3:
            if contenido[i] == "/":
                estado = 0
                lexemaAuxiliar += contenido[i]
                ventana.pintar(lexemaAuxiliar,"comentario")
                lexemaAuxiliar = ""
            else:
                estado = 2
                i -= 1
        elif estado == 4:
            if contenido[i] == "-" or contenido[i].isalpha() or contenido[i].isdigit():
                lexemaAuxiliar += contenido[i]
                estado = 4
                recorrido += "4, "
            else:
                if lexemaAuxiliar.lower() == "color":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_color",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "border":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    listadoTokens.append(Token("tk_border",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    estado = 0
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "text-align":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    listadoTokens.append(Token("tk_textAlign",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    estado = 0
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-weight":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_fontWeight",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-left":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_paddingLeft",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-top":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_paddingTop",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "line-height":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_lineHeight",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-top":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_marginTop",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-left":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_marginLeft",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "display":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_display",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "top":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_top",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "float":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_float",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "min-width":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_minWidth",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "background-color":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_backgroundColor",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "opacity":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_opacity",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-family":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_fontFamily",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-size":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_fontSize",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-right":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_paddingRight",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_padding",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "width":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_width",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-right":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_marginRight",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_margin",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "position":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_position",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "right":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_right",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "clear":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_clear",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "max-height":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_maxHeight",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "background-image":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_backgroundImage",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "background":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_background",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font-style":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_fontStyle",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "font":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_font",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "padding-bottom":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_paddingBottom",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "height":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_height",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "margin-bottom":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_marginBottom",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "border-style":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_borderStyle",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "bottom":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_bottom",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "left":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_left",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "max-width":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_maxWidth",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "min-height":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_minHeight",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "px":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_px",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "em":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_em",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "vh":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_vh",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "vw":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_vw",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "in":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_in",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "cm":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_cm",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "mm":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_mm",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "pt":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_pt",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "pc":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_pc",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "content":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_content",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                elif lexemaAuxiliar.lower() == "url":
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"reservada")
                    estado = 0
                    listadoTokens.append(Token("tk_url",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
                    recorrido = ""
                    i -= 1
                else:
                    contenidoSalida += lexemaAuxiliar
                    ventana.pintar(lexemaAuxiliar,"variable")
                    estado = 0
                    listadoTokens.append(Token("tk_id",recorrido.strip(", "),lexemaAuxiliar))
                    lexemaAuxiliar = ""
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
                listadoTokens.append(Token("tk_numero", recorrido.strip(", "),lexemaAuxiliar))
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"intBoolean")
                lexemaAuxiliar = ""
                recorrido = ""
                estado = 0
                i -= 1
        elif estado == 6:
            if contenido[i].isdigit():
                estado = 6
                lexemaAuxiliar += contenido[i]
                recorrido += "6, "
            else:
                listadoTokens.append(Token("tk_numeroDecimal", recorrido.strip(", "),lexemaAuxiliar))
                contenidoSalida += lexemaAuxiliar
                ventana.pintar(lexemaAuxiliar,"intBoolean")
                lexemaAuxiliar = ""
                recorrido = ""
                estado = 0
                i -= 1
        elif estado == 7:
            if contenido[i] == "\"" or contenido[i] == "“":
                estado = 0
                contenidoSalida += lexemaAuxiliar
                contenidoSalida += contenido[i]
                ventana.pintar(lexemaAuxiliar,"otro")
                ventana.pintar("\"","otro")
                lexemaAuxiliar = ""
                listadoTokens.append(Token("tk_comillas","0",contenido[i]))
            else:
                estado = 7
                lexemaAuxiliar += contenido[i]
        i += 1

    ventana.mostrarRecorrido(listadoTokens)
    ventana.mostrarErrores(listadoErrores)
    ventana.reporteDeErroresTabla(listadoErrores, "/ErroresLexicosCSS.html")
    generarArchivoSalida(contenidoSalida, path)


def generarArchivoSalida(contenido, path):
    archivo = open(path,"w")
    archivo.write(contenido)
