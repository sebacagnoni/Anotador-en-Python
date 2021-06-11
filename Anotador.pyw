from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog

import os


#Raiz

root = Tk()

root.title("Agenda de ideas y obligaciones")
root.iconbitmap("pencil-icon-vector.ico")
root.geometry("500x500")
root.config(bg = "#3CAFAA")

#Frame
#Frames

frame1 = Frame()
frame1.config(width = "1500", height = "500")
frame1.config(bg = "#3CAF7A")
frame1.config(bd = 35)
frame1.pack(side = "top")

#Funciones Menu---------------------------------------------------------

def salir():
	valor = messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")
	if valor == "yes":
		root.destroy()

def cerrarHijo(v0):
	v0.destroy()



def acercaDe():
    messagebox.showinfo("Anotador digital", "Anotador version 1.0 \n creado por Sebastian S Cagnoni")	


def licencia():
	messagebox.showinfo("Anotador version 1.0", "Producto bajo Licencia GNU")


def onOpen():
	archivo = filedialog.askopenfilename(initialdir = "C:/", title = "open file", filetypes = (("Archivos de Texto", "*.txt"), ("Archivos PDF", "*.pdf" ), ("Todos los Archivos", "*.*"))) #Abrir
	print(archivo) #imprime la ruta del archivo en la consola

def onSave(): 
    print(filedialog.asksaveasfilename(initialdir = "C:/", title = "open file", filetypes = (("Archivos de Texto", "*.txt"), ("Archivos PDF", "*.pdf" ), ("Todos los Archivos", "*.*")))) #Guardar

def resetProgram():
	python = sys.executable
	os.execl(python, python, * sys.argv)#Solucionar

def Nuevo():
   		v0 = Toplevel(root)
   		v0.geometry("750x500")
   		v0.config(bg = "#3CAFAA")

   		frame2 = Frame(v0)
   		frame2.config(width = "800", height = "300")
   		frame2.config(bg = "#3CAF7A")
   		frame2.config(bd = 35)
   		frame2.pack(side = "top")
   		nombreLabel = Label(frame2, text = "Nombre:", font = ("Handle Drawn Alphabet", 15))
   		nombreLabel.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)

   		cuadroNombre = Entry(frame2)
   		cuadroNombre.grid(row = 0, column = 1, sticky = "e", padx = 10, pady = 10)


   		quehacerLabel = Label(frame2, text = "Lista de quehaceres", font = ("Handle Drawn Alphabet", 11))
   		quehacerLabel.grid(row = 1, column = 1, sticky = "e", padx = 10, pady = 10)

 	  	cuadroQuehacer = Text(frame2, width = 20, height = 16)
   		cuadroQuehacer.grid(row = 2, column = 1, sticky = "e", padx = 10, pady = 10)

   		ideasLabel = Label(frame2, text = "Mis ideas", font = ("Handle Drawn Alphabet", 11))
   		ideasLabel.grid(row = 1, column = 3, sticky = "e", padx = 10, pady = 10)

   		cuadroIdeas = Text(frame2, width = 20, height = 16)
   		cuadroIdeas.grid(row = 2, column = 3, sticky = "e", padx = 10, pady = 10)

   		scrollVert = Scrollbar(frame2, command = cuadroQuehacer.yview)
   		scrollVert.grid(row = 2, column = 2, sticky = "nsew")
   		cuadroQuehacer.config(yscrollcommand = scrollVert.set)

   		scrollVert2 = Scrollbar(frame2, command = cuadroIdeas.yview)
   		scrollVert2.grid(row = 2, column = 4, sticky = "nsew")
   		cuadroIdeas.config(yscrollcommand = scrollVert2.set)	
   #-----------------Menu Hijo-----------------------------------------
   		barraMenu = Menu()
   		v0.config(menu = barraMenu, width = 300, height = 300)

   		archivoMenu = Menu(barraMenu, tearoff = 0)
   		archivoMenu.add_command(label = "Abrir", command = onOpen)
   		archivoMenu.add_command(label = "Guardar", command = onSave)
   		archivoMenu.add_command(label = "Guardar Como")
   		archivoMenu.add_separator() #linea separadora
   		archivoMenu.add_command(label = "Cerrar", command = lambda:cerrarHijo(v0))
   		

   		barraMenu.add_cascade(label = "Archivo",      menu = archivoMenu)





#MENU--------------------------------------------------------------------


barraMenu = Menu()
root.config(menu = barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Abrir", command = onOpen)
archivoMenu.add_command(label = "Nuevo", command = Nuevo)
archivoMenu.add_command(label = "Guardar", command = onSave)
archivoMenu.add_command(label = "Guardar Como")
archivoMenu.add_separator() #linea separadora
archivoMenu.add_command(label = "Cerrar")
archivoMenu.add_command(label = "Salir", command = salir)

archivoEdicion = Menu(barraMenu, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoAyuda = Menu(barraMenu, tearoff = 0)
archivoAyuda.add_command(label = "Licencia", command = licencia)
archivoAyuda.add_command(label = "Acerca de...", command = acercaDe )

#----Barra Menu--------------------------------------------------

barraMenu.add_cascade(label = "Archivo",      menu = archivoMenu)
barraMenu.add_cascade(label = "Edición",      menu = archivoEdicion)
barraMenu.add_cascade(label = "Ayuda",        menu = archivoAyuda)

#-----------------------------------------------------------------









#botones y entrys-----------------------------------------------------




#---------------------------------------------------------------------

def codigoBoton():
	pass


botonSave = Button(root, text = "guardar", command = codigoBoton)
botonSave.pack()

#se desconfiguro el nombreLabel, alinearlo

#---------------------------------Ventana Hija---------------------------------------





root.mainloop()