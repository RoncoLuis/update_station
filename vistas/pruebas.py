"""
probando cosas de tkinter
"""
from tkinter import *
from tkinter import messagebox

raiz = Tk() #crea una nueva ventana raiz

def muestra_info():
    messagebox.showinfo("update station","conectado con exito")

def cambiar_ventana():
    print('hola mundo con boton')

barra_menu = Menu(raiz)
#a partir de aqui se puede configurar todos los elementos de la raiz
raiz.title("Update Station") #titulo del frame
raiz.iconbitmap("../img/update_icon.ico") #anadiendo un icono al frame
raiz.config(bg="green",menu=barra_menu)

#agregando barra menu para salir de la aplicacion
opcion_menu = Menu(barra_menu)
opcion_menu.add_command(label='Salir')

#anadiendo elemento interno a la ventana raiz, se le conoce como frame
miframe = Frame()
miframe.pack(fill='both',expand='True') #con este metodo el frame se pega a la raiz
miframe.config(bg="green",width="600",height="400")

#agregando elementos dentro del frame
logo = PhotoImage(file='../img/update_logo_450px.gif')
Label(miframe,image=logo).place(x=80,y=50) #funciona como el pack. Pero no redimenciona el frame, respeta las medidas

#agregando boton de conectar con la siguiente ventana
btn_conectar = Button(raiz,text='Conectar',command=muestra_info)
btn_conectar.pack()

raiz.mainloop() #este loop es para que la ventana no se cierre