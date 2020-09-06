import os 
import webbrowser

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from analizadorHtml import obtenerContenido
from analizadorCSS import obtenerContenidoCSS
from analizadorJS import obtenerContenidoJS

#inicializacion del objeto que contiene la ventana
ventana = Tk()

#instancias de las cajas de texto de salida
cajaDeTexto = Text(ventana,height = 52, width = 90)
consola = Text(ventana,height = 52, width = 93)

#variable que almacena el path de entrada y salida
path = ""
pathSalidaLinux = ""

def mostrarVentana():
    #asignacion de tamaño de la ventana
    ventana.geometry("1500x900")

    #asignacion del titulo de la ventana
    ventana.title("OLC Proyecto 1")

    #creando una instancia de un menu
    navbar = Menu(ventana)
    
    #agregando las opciones al menu
    navbar.add_command(label = "Nuevo", command = lambda: limpiar(1))
    navbar.add_command(label = "Abrir", command = abrirArchivo)
    navbar.add_command(label = "Guardar")
    navbar.add_command(label = "Guardar como")
    navbar.add_command(label = "Ejecutar analisis", command = analizarArchivo)
    navbar.add_command(label = "Salir", command = ventana.quit)
    
    #asignando el menu a la ventana
    ventana.config(menu = navbar)
    
    #instancia de la caja de texto  
    cajaDeTexto.grid(row = 100, column = 100)
    cajaDeTexto.place(x = 5, y = 0)  

    #instancia de la consola de salida
    consola.grid(row = 100, column = 100)
    consola.place(x = 743, y=0)

    #mostrando la ventana
    ventana.mainloop()

def abrirArchivo():
    global path

    #abriendo un seleccionador de archivos
    path = filedialog.askopenfilename(title = "Seleccione el archivo a analizar", filetypes = [("archivos de analisis","*.html *.js *.css *.rmt")]) 
    
    #validando que se haya escogido algun archivo para analizar
    if path == ():
        path = ""
        messagebox.showerror("Error","Debe de seleccionar un archivo para ser analizado")

def analizarArchivo():
    global path

    #validacion de la existencia del path de entrada
    if path != "":
        #obtencion de la extension del archivo
        desicion = os.path.basename(path).split(".")

        #validacion de ejecucion del tipo de analizador correspondiente al archivo
        if desicion[1].lower() == "html":
            limpiar(0)
            obtenerContenido(path)
        elif desicion[1].lower() == "css":
            limpiar(0)
            obtenerContenidoCSS(path)
        elif desicion[1].lower() == "js":
            limpiar(0)
            obtenerContenidoJS(path)
        elif desicion[1].lower() == "rmt":
            limpiar(0)
            print("sintactico")
    else:
        messagebox.showerror("Error","Aun no se a seleccionado ningun archivo para analizar")

def limpiar(tipo):
    global path

    cajaDeTexto.delete("1.0","end")
    consola.delete("1.0","end")
    
    if tipo != 0:
        path = ""

def pintar(contenido, identificador):
    cajaDeTexto.insert(INSERT, contenido, identificador)
    cajaDeTexto.tag_config('entreEtiquetas', foreground = "black")
    cajaDeTexto.tag_config('reservada', foreground = "red")
    cajaDeTexto.tag_config('variable', foreground = "green")
    cajaDeTexto.tag_config('otro', foreground = "black")
    cajaDeTexto.tag_config('stringChar', foreground = "gold")
    cajaDeTexto.tag_config('comentario', foreground = "gray")
    cajaDeTexto.tag_config('intBoolean', foreground = "blue")
    cajaDeTexto.tag_config('operador', foreground = "DarkOrange1")

def mostrarRecorrido(listadoTokens):
    consola.insert(INSERT,"|---------------Reporte de tokens----------------|\n")
    insercion = ""
    iterador = 1
    for i in listadoTokens:
        insercion += str(iterador)+". Token: "+i.tipoToken+" Valor: "+i.valor+" Recorrido: "+i.recorrido+"\n"
        consola.insert(INSERT,insercion)
        insercion = ""
        iterador += 1

def mostrarErrores(listadoErrores):
    consola.insert(INSERT,"\n|---------------Reporte de errores----------------|\n")
    insercion = ""
    iterador = 1
    for i in listadoErrores:
        insercion += str(iterador)+". Fila: "+str(i.fila)+" Columna: "+str(i.columna)+" Error: "+i.error+"\n"
        consola.insert(INSERT,insercion)
        insercion = ""
        iterador += 1

def obtenerPathSalidaLinux(linea1:str, linea2):
    global pathSalidaLinux

    if linea1.lower().find("pathl") != -1:
        pos = linea1.lower().find("/")
        pathSalidaLinux = linea1[pos:len(linea1)]
        pathSalidaLinux = pathSalidaLinux.rstrip("\n")
        pathSalidaLinux = pathSalidaLinux.rstrip("*/")
        pathSalidaLinux = pathSalidaLinux.rstrip(" ")
    else:
        pos = linea2.lower().find("/")
        pathSalidaLinux = linea2[pos:len(linea2)]
        pathSalidaLinux = pathSalidaLinux.rstrip("\n")
        pathSalidaLinux = pathSalidaLinux.rstrip("*/")
        pathSalidaLinux = pathSalidaLinux.rstrip(" ")

def obtenerDirectorioActual():
    return os.path.dirname(os.path.abspath(__file__))

def reporteDeErroresTabla(listado, tipo):
    pathSalida = obtenerDirectorioActual() + tipo
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

    for error in listado:
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
    abrirReporte(pathSalida)

def abrirReporte(path):
    webbrowser.open(path)