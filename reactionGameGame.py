import pyautogui
import tkinter as tk
import sqlite3
import time


def spawnNewButton():
    global x
    x=x+50
    global y
    y=y+50
    gameButton.place(x=x, y=y)

    
def clicked():
    print("pooPooPeepee")
    gameButton.place_forget()
    spawnNewButton()

#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#
global gameButton
gameButton= tk.Button(
        window,
        width=10,
        height=5, 
        background="red",
        command=clicked 
    )

x=100
y=100
startTime=time.time()
spawnNewButton()
