from tkinter import *
from tkinter import messagebox
import Anotador

def salir():
	valor = messagebox.askquestion("Salir", "Estas seguro que deseas salir de la aplicación?")
	if valor == "yes":
		return True
	else:
	    return False	