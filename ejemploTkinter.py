#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd


def saludar():

	resultado = sd.askstring("consulta", "Cual es su nombre?")
	mb.showinfo("resultado" , str(resultado))
	
	resultado = sd.askinteger("consulta", "su edad?")
	mb.showwarning("resultado" , str(resultado))

	resultado = sd.askfloat("consulta", "su altura?")
	mb.showerror("resultado" , str(resultado))
	
	resultado = mb.askokcancel("consulta", "No te gusta python?")
	mb.showinfo("resultado" , str(resultado))

mainForm = tk.Tk()
mainForm.title("Hola tkinter")
mainForm.geometry("400x200")

botonSaludar = tk.Button(mainForm, text = "Consulta", command = saludar)
botonSaludar.place(x = 10, y = 10)

mainForm.mainloop()
