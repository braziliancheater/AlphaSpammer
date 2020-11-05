#simple simple example of a spammer?
#Made from ground by brazilian aka crim3s
import pyautogui, time, pymsgbox, ctypes
from pynput.mouse import Listener
from ctypes import wintypes

user32 = ctypes.windll.user32
h_wnd = user32.GetForegroundWindow()
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))

f = open("text",'r')

print("   ___   __     __        ")
print("  / _ | / /__  / /  ___ _ ")
print(" / __ |/ / _ \/ _ \/ _ `/ ")
print("/_/ |_/_/ .__/_//_/\_,_(_)")
print("       /_/                ")

print("\nAlpha Spammer 0.1 by brazilian")

time.sleep(3)

print("\nMetodos: ")
print("Generic Spam (PyAutoGUI) - 1")
print("Email Nuker - 2")
print("...")
d = int(input("Escolha - "))

if d == 1:
    b = int(input("Delay (Segundos) - "))
    c = int(input("Numero de Repeticoes - "))
    if d == 1:
        print("Selecione a Janela principal - \n")
        time.sleep(3)
        print(pid.value)
        print("...\n")
                
        for word in f:
            for i in range(c):
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                time.sleep(b)
    #if you want to use a prompt box
    #pymsgbox.alert('Done..', 'Alpha')
if d == 2:
    #todo email nuker
    print("not done yet")
    time.sleep(3)
    exit()