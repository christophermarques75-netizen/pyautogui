import pyautogui
import time

def automatizar_001():
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.press('backspace')
    pyautogui.write(r"code C:\Users\CHRISTOPHERGABRIELMA\Desktop\tudo\pyautogui")
    time.sleep(1)
    pyautogui.press("enter")


def automatizar_002():
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.press('backspace')
    pyautogui.write(r"code C:\Users\CHRISTOPHERGABRIELMA\Desktop\tudo\hora de codar")
    time.sleep(1)
    pyautogui.press("enter")
