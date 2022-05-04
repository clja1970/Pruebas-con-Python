'''
Created on 19 feb. 2022

@author: anka
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 

from tkinter import Tk, PhotoImage, Label

import tkinter as tk


#Importante import para una mejor configuración
# definicioón de funciones con los botones
def lucesamarillas():
    print(10109)
    
def lucesrojas():
    print("Luces rojas encendidas")
    
def apagaamarilla():
    print("Apagadas luces amarillas")
    
def apagarojas():
    print("Luces rojas apagadas")

# Define la ventana principal de la aplicación
raiz = Tk()

# Define las dimensiones de la ventana, que se ubicará en 
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella. 

raiz.geometry('400x400') # anchura x altura


# Asigna un título a la ventana

raiz.title('Tesa Marchena')

# Lees la imagen:
# He colocado ruta relativa, es decir, la imagen a la misma 
# altura de la aplicación. Si prefieres, puedes colocar una
# ruta absoluta.

raiz.iconbitmap('ic_launcher.ico')
#Ojo el icono en linux no funciona

imagen = PhotoImage(file = "Tesa.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")

background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

background.config(bg = "beige")

# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris
#raiz.configure(bg='beige')

raiz.resizable(False, False)


# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón


tk.Button(raiz, text='Salir', foreground="#ff0000", background="#000000", command=quit).pack(side=tk.BOTTOM)
tk.Button(raiz, text='Apagar luces rojas', background="#ff0000", command=apagarojas).pack(side=tk.BOTTOM)
tk.Button(raiz, text='Apagar luces amarilas', background="#f8ff3b", command=apagaamarilla).pack(side=tk.BOTTOM)
tk.Button(raiz, text='Encender luces amarilas', background="#f8ff3b", command=lucesamarillas).pack(side=tk.TOP)
tk.Button(raiz, text='Encender luces rojas', background="#ff0000", command=lucesrojas).pack(side=tk.TOP)


# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de 
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.


raiz.mainloop()