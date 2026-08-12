from tkinter import *
from tkinter import ttk
import pyautogui
import time

def automatizar():
    pyautogui.hotkey("win", "r")
    pyautogui.write("cmd")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=774, y=407)
    time.sleep(5)
    pyautogui.write("cd Desktop")
    pyautogui.press("enter")
    pyautogui.write("cd Tudo")
    pyautogui.press("enter")
    pyautogui.write("cd pyautogui")
    pyautogui.press("enter")
    pyautogui.write("code .")
    pyautogui.press("enter")
    
root = Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

ttk.Button(frm, text="abrir o vs com a pasta atual", command= lambda: automatizar()).grid(column=1, row=0)


root.mainloop()