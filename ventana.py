import os 
import webbrowser

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from analizadorHtml import obtenerContenido
from analizadorCSS import obtenerContenidoCSS
from analizadorJS import obtenerContenidoJS
from analizadorOperaciones import obtenerContenidoOperaciones

#inicializacion del objeto que contiene la ventana
ventana = Tk()

#instancias de las cajas de texto de salida
cajaDeTexto = Text(ventana,height = 52, width = 90)
consola = Text(ventana,height = 52, width = 93)

#dejando de lectura la consola
#consola.configure(state=DISABLED)

#variable que almacena el path de entrada y salida
path = ""
pathSalidaLinux = ""
nombreArchivo = ""

def mostrarVentana():
    #tamaño de la ventana
    anchuraVentana = 1500
    alturaVentana = 905

    #centrada de la ventana en la pantalla
    posX = (ventana.winfo_screenwidth() - anchuraVentana)/2
    posY = (ventana.winfo_screenheight() - alturaVentana)/2
    ventana.geometry('%dx%d+%d+%d' % (anchuraVentana, alturaVentana, posX, posY))

    #asignacion del titulo de la ventana
    ventana.title("OLC Proyecto 1")

    #creando una instancia de un menu
    navbar = Menu(ventana)
    
    #agregando las opciones al menu
    navbar.add_command(label = "Nuevo", command = lambda: limpiar(1))
    navbar.add_command(label = "Abrir", command = abrirArchivo)
    navbar.add_command(label = "Guardar", command = guardaArchivo)
    navbar.add_command(label = "Guardar como", command = guardarComoArchivo)
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
    else:
        #si el archivo existe colocar su contenido en el text box
        archivo = open(path,"r")
        contenidoArchivo = ""
        for linea in archivo.readlines():
            contenidoArchivo += linea
        cajaDeTexto.insert(INSERT,contenidoArchivo)

def guardaArchivo():
    global path

    if path != "":
        #obtener el contenido del text box y reemplazarlo por el actual del archivo
        textoCaja = cajaDeTexto.get("1.0",END)
        archivoGuardar = open(path,"w")
        archivoGuardar.write("")
        archivoGuardar.write(textoCaja)
        archivoGuardar.close()
        messagebox.showinfo("Anuncio", "Se han realizado los cambios en el archivo exitosamente")
    else:
        messagebox.showerror("Error","Debe de cargar un archivo previamente para poder modificarlo")

def guardarComoArchivo():
    archivoGuardarComo = filedialog.asksaveasfile(mode = "w")
    #validando que se haya seleccionado lo necesario para guardar el archivo
    if archivoGuardarComo is None:
        messagebox.showerror("Error","Debe de llenar los campos correspondientes para guardar el archivo")
    textoCaja = cajaDeTexto.get("1.0", END)
    archivoGuardarComo.write(textoCaja)
    archivoGuardarComo.close()
    messagebox.showinfo("Anuncio", "Se ha guardado el nuevo archivo exitosamente")

def analizarArchivo():
    global path, nombreArchivo

    #validacion de la existencia del path de entrada
    if path != "":
        #obtencion de la extension del archivo
        desicion = os.path.basename(path).split(".")

        #validacion de ejecucion del tipo de analizador correspondiente al archivo
        if desicion[1].lower() == "html":
            limpiar(0)
            dividido = os.path.split(path)
            nombreArchivo = dividido[1]
            obtenerContenido(path)
        elif desicion[1].lower() == "css":
            limpiar(0)
            dividido = os.path.split(path)
            nombreArchivo = dividido[1]
            obtenerContenidoCSS(path)
        elif desicion[1].lower() == "js":
            limpiar(0)
            dividido = os.path.split(path)
            nombreArchivo = dividido[1]
            obtenerContenidoJS(path)
        elif desicion[1].lower() == "rmt":
            limpiar(0)
            obtenerContenidoOperaciones(path)
            messagebox.showinfo("Anuncio", "Se han terminado de analizar las operaciones aritmeticas")
    else:
        messagebox.showerror("Error", "Aun no se a seleccionado ningun archivo para analizar")

def limpiar(tipo):
    global path, pathSalidaLinux, nombreArchivo

    #limpiando los text box por completo
    cajaDeTexto.delete("1.0","end")
    consola.delete("1.0","end")
    
    #reiniciando los path para analizar un nuevo archivo
    if tipo != 0:
        path = pathSalidaLinux = nombreArchivo = ""

def pintar(contenido, identificador):
    #insertando el contenido a la text box
    cajaDeTexto.insert(INSERT, contenido, identificador)
    
    #reglas de colores dependiendo del tipo de token que es
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

def obtenerPathSalidaLinux(linea1, linea2):
    global pathSalidaLinux

    if linea1.lower().find("pathl") != -1:
        #obteniendo la posicion donde se encuentra el verificador que indica que es un path 
        #de linux
        pos1 = linea1.lower().find("pathl")

        #creando el substring nuevo que almacena la cadena del path linux
        linea1 = linea1[pos1: len(linea1)]
        
        #encontrando la posicion de la palabra output
        pos = linea1.lower().find("output")
        
        #creando el nuevo substring que almacena la cadena del path de linux
        pathSalidaLinux = linea1[pos:len(linea1)]
        
        #recorriendo la cadena del path de forma inversa hasta encontrar una diagonal para limpiar
        #de posibles errores
        iterador = len(pathSalidaLinux)-1
            
        while True:
            if pathSalidaLinux[iterador] == "/":
                break
            iterador -= 1
        
        #asignando la nueva cadena limpia a la variable
        pathSalidaLinux = os.path.join(obtenerDirectorioActual(), pathSalidaLinux[:iterador]) 
    else:
        pos1 = linea2.lower().find("pathl")
        linea2 = linea2[pos1: len(linea2)]
        pos = linea2.find("output")
        pathSalidaLinux = linea2[pos:len(linea2)]
        iterador = len(pathSalidaLinux)-1
        while True:
            if pathSalidaLinux[iterador] == "/":
                break
            iterador -= 1
        pathSalidaLinux = os.path.join(obtenerDirectorioActual(), pathSalidaLinux[:iterador]) 

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

def guardarArchivoAnalizado(contenido):
    global pathSalidaLinux, nombreArchivo
    #comando para crear todas las carpetas necesarias en linux
    comando = "mkdir -p "+ pathSalidaLinux
    os.system(comando)
    pathSalidaLinux = os.path.join(pathSalidaLinux, nombreArchivo)
    archivo = open(pathSalidaLinux,"w")
    archivo.write(contenido)
    archivo.close()

def abrirReporte(path):
    webbrowser.open(path)