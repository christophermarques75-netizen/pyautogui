from tkinter import *
from tkinter import ttk
import time
from auxiliar_de_autenticação import *
root = Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()

ttk.Label(frm, text="boa tarde meu lindo bora pra mais um dia").grid(column=0, row=0)

ttk.Button(frm, text="abrir o vs com a pasta do git particular",command= lambda: automatizar_001()).grid(column=0, row=1)
ttk.Button(frm, text="abrir o vs com a pasta do projeto integrador", command= lambda: automatizar_002()).grid(column=0, row=2)

root.mainloop()