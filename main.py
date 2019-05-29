from gi.repository import Gtk
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image
from calculate import *

#Crea ventana
window =Tk()
#Titulo de la ventana
window.title("Sistema de estimación de pasajeros Transmilenio")
    #Tamaño Ventana
window.geometry('1200x780')
    #Label con mensaje
lbl=Label(window, text="Bienvenido al sistema de estimación de pasajeros en trasmilenio,\n por favor, seleccione la troncal e ingrese\n la hora en formato militar que desea visualizar\n"
,font=("Arial",14))
     #ubicaacion del mensajee
lbl.grid(column=0, row=0)
#Definicion de funcion a ejecutar cuando se haga click en el boton
def clicked():
    #Accion a realizar cuando se hace click en el boton
    #Cambia el texto de la primera label, llamada lbl
    #lbl.configure(text="Me clickeaste We!!")
    #creo un mensaje en un string con el contenido del cuadro de texto de nombre msg
    n=int(spin.get())
    p=int(spin2.get())
    f=get_filename(combo.get())
    ###
    dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
    Gtk.ButtonsType.OK, "Troncal " +combo.get())
    dialog.format_secondary_text(get_diferencia(n,p,f))
    dialog.run()
    ###

#definicion del boton, texto, color y accion
btn = Button(window, text="Comparar hora 1 vs hora 2", command=clicked)
 #Ubicacion del boton
btn.grid(column=1, row=3)
btn.place(x=560,y=140)


#CreaBoton llamado calcular que abre una imagen llamada SPY
Calcular=tk.Button(text="Calcular flujo estacion en hora 1", width=25,command=lambda:ImageShow("graph.png"))
#Ubicacion de boton
Calcular.place(x=190,y=180)
#Funcion que se activa al presionar el boton que carga la imagen
def ImageShow(path):
        #Aqui se puede poner la funcion de Calcular
        n=spin3.get()
        f=get_filename(combo.get())
        msg= "Se espera que en la troncal " +combo.get()+" a las "+n+" tenga una afluencia de "+str(get_cantidad(n,f))
        get_plot(n,f)
        lbl2=Label(window,text=msg)
        lbl2.place(x=360, y=230)
        #Abre la imagen segun el camino que se indica en el path del boton
        print(path)
        image = Image.open(path)
        #Carga la imagen en un formato que peude abrir Tkinter
        photo = ImageTk.PhotoImage(image)
        #Carga la imagen como un label
        label = tk.Label( image=photo, bg="black")
        #Mantiene continuas invocaciones para que el garbage collector no la borre
        label.image = photo
        #Ubicacion de la imagen en la ventana
        label.place(x=350, y=280)
     #Declaracion de un combobox llamado combo
combo = Combobox(window)
    #Valores que toma el combo box
combo['values']= ("Av americas Occ-Or","Av americas Or-Occ","Suba N-S","Suba S-N", "Calle 80 Or-Occ",
     "Calle 80 Occ-Or","Cacacas N-S","Cacacas S-N","Calle 26 Occ-Or","Calle 26 Or-Occ","NQS-Soacha N-S",
     "NQS-Soacha S-N","Auto norte N-S","Auto norte S-N")
     ##Valor inicial
combo.current(0) #set the selected item
     #Ubicacion Combobox
combo.grid(column=0, row=2)

#spin hora
spinlbl=Label(window, text="    Hora" ,font=("Arial",12))
#ubicaacion del mensajee
spinlbl.grid(column=0, row=3)
spin3 = Spinbox(window, from_=5, to=22, width=4)
spin3.grid(column=0,row=4)

spinlbl=Label(window, text="     Hora 1",font=("Arial",12))
spinlbl.grid(column=1, row=1)

spinlbl=Label(window, text="     Hora 2",font=("Arial",12))
spinlbl.grid(column=3, row=1)

spin = Spinbox(window, from_=5, to=22, width=8)
spin.grid(column=1,row=2)

spin2 = Spinbox(window, from_=5, to=22, width=8)
spin2.grid(column=3,row=2)

     #Creacion de la GUI
window.mainloop()
#Referencias:
#https://likegeeks.com/es/ejemplos-de-la-gui-de-python/
