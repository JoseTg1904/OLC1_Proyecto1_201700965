import os 
import platform

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from analizadorHtml import obtenerContenido


#inicializacion del objeto que contiene la ventana
ventana = Tk()

def mostrarVentana():
    #asignacion de tamaño de la ventana
    ventana.geometry("1500x900")

    #asignacion del titulo de la ventana
    ventana.title("OLC Proyecto 1")

    #creando una instancia de un menu
    navbar = Menu(ventana)
    
    #agregando las opciones al menu
    navbar.add_command(label = "Nuevo")
    navbar.add_command(label = "Abrir", command = abrirArchivo)
    navbar.add_command(label = "Guardar")
    navbar.add_command(label = "Guardar como")
    navbar.add_command(label = "Ejecutar analisis")
    navbar.add_command(label = "Salir", command = ventana.quit)
    
    #asignando el menu a la ventana
    ventana.config(menu = navbar)
    
    #mostrando la ventana
    ventana.mainloop()

def abrirArchivo():
    #abriendo un seleccionador de archivos
    path = filedialog.askopenfilename(title = "Seleccione el archivo a analizar", filetypes = [("archivos de analisis","*.html *.js *.css")]) 
    if path != ():
        #obtencion de la extension del archivo
        desicion = os.path.basename(path).split(".")

        #validacion de ejecucion del tipo de analizador correspondiente al archivo
        if desicion[1].lower() == "html":
            obtenerContenido(path)
        elif desicion[1].lower() == "css":
            print("css")
        elif desicion[1].lower() == "js":
            print("js")
    else:
        messagebox.showerror("Error","Debe de seleccionar un archivo para ser analizado")