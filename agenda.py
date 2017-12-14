#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from saveLoad import *
from json import loads
from json import dump

def addPerson(diary, person):
	row = {}
	
	for field in person:
		row[field] = sd.askstring("Alta de Personas", "Ingrese " + field)
	
	diary.append(row)
	
	with open("diary.json", "w") as fout:
		dump(diary, fout)

def mostrarALoIndio(diary):
	for persona in diary:
		mb.showinfo("Datos", persona)

diary = loads(open("diary.json").read())
person = ("Nombre", "Edad", "DNI")

mainForm = tk.Tk()
mainForm.title("Hola tkinter")
mainForm.geometry("400x200")

buttonHight = tk.Button(mainForm, text = "Ingresar datos", command = lambda: addPerson(diary, person))
buttonHight.place(x = 10, y = 10)

buttonShow = tk.Button(mainForm, text = "Mostrar datos", command = lambda: mostrarALoIndio(diary))
buttonShow.place(x = 10, y = 50)

mainForm.mainloop()
	
	
	
	
	
	
	
	
	
	
	
	
