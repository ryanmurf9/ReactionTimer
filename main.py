import pyautogui
import tkinter as tk
import sqlite3
import time
import random

screenW, screenH = pyautogui.size()


resolution=str(screenW)+"x"+str(screenH)

window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#Must be in window.geometry("500x500") format
#import reactionGameMenu


state='game'
running=True


while running:
    if state=='menu':
        import reactionGameMenu
    if state=='game':
        from reactionGameGame import Button
        startTime=time.time()
        button=Button(10, 5, "red",0,startTime)  
    if state=='score':
        import reactionGameScores
    window.mainloop()
#Kill program


