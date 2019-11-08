"""
Ventana principal UpdateStation
@LuisR
Esta ventana se enlaza con video_recorder.py
"""
from tkinter import *

principal = Tk()
principal.geometry("600x400+100+100")
principal.title("Update Station")
#etiqueta logo update station
lbl_logo = Label(text="label").place(x=100,y=20)
#lbl_logo.pack()

principal.mainloop()




