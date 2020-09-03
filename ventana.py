import os 

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from analizadorHtml import obtenerContenido
from analizadorCSS import obtenerContenidoCSS
from analizadorJS import obtenerContenidoJS

#inicializacion del objeto que contiene la ventana
ventana = Tk()

cajaDeTexto = Text(ventana,height = 52, width = 90)
consola = Text(ventana,height = 52, width = 93)

def mostrarVentana():
    #asignacion de tamaño de la ventana
    ventana.geometry("1500x900")

    #asignacion del titulo de la ventana
    ventana.title("OLC Proyecto 1")

    #creando una instancia de un menu
    navbar = Menu(ventana)
    
    #agregando las opciones al menu
    navbar.add_command(label = "Nuevo", command = limpiar)
    navbar.add_command(label = "Abrir", command = abrirArchivo)
    navbar.add_command(label = "Guardar")
    navbar.add_command(label = "Guardar como")
    navbar.add_command(label = "Ejecutar analisis")
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
    #abriendo un seleccionador de archivos
    path = filedialog.askopenfilename(title = "Seleccione el archivo a analizar", filetypes = [("archivos de analisis","*.html *.js *.css *.rmt")]) 
    if path != ():
        #obtencion de la extension del archivo
        desicion = os.path.basename(path).split(".")

        #validacion de ejecucion del tipo de analizador correspondiente al archivo
        if desicion[1].lower() == "html":
            limpiar()
            obtenerContenido(path)
        elif desicion[1].lower() == "css":
            limpiar()
            obtenerContenidoCSS(path)
        elif desicion[1].lower() == "js":
            limpiar()
            obtenerContenidoJS(path)
        elif desicion[1].lower() == "rmt":
            limpiar()
            print("sintactico")
    else:
        messagebox.showerror("Error","Debe de seleccionar un archivo para ser analizado")

def limpiar():
    cajaDeTexto.delete("1.0","end")
    consola.delete("1.0","end")

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

def obtenerPathLinux(linea1, linea2):
    pass