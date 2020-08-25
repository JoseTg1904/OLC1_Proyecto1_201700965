from tkinter import *
from tkinter import filedialog
import os 

ventana = Tk()

def mostrarVentana():
    ventana.geometry("1500x900")
    ventana.title("OLC Proyecto 1")
    navbar = Menu(ventana)
    ventana.config(menu = navbar)
    navbar.add_command(label = "Nuevo")
    navbar.add_command(label = "Abrir", command = abrirArchivo)
    navbar.add_command(label = "Guardar")
    navbar.add_command(label = "Guardar como")
    navbar.add_command(label = "Ejecutar analisis")
    navbar.add_command(label = "Salir", command = ventana.quit)
    ventana.mainloop()

def abrirArchivo():
    path = filedialog.askopenfilename(title = "Seleccione el archivo a analizar", filetypes = [("archivos de analisis","*.html *.js *.css") ]  ) 
    desicion = os.path.split(path)
    desicion = desicion[1].split(".")
    if desicion[1].lower() == "html":
        print("html")
    elif desicion[1].lower() == "css":
        print("css")
    elif desicion[1].lower() == "js":
        print("js")