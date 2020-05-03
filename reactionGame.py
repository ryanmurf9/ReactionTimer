import pyautogui
import tkinter as tk
import sqlite3

screenW, screenH = pyautogui.size()


window = tk.Tk()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.insert(0, "Username")
entry.pack()

label = tk.Label(
    text="Reaction Test",
    foreground="white",  
    background="black"  
)
label.pack()
gameButton = tk.Button(
    text="To Go To Game",
    width=25,
    height=5,
    bg="white",
    fg="black",
)
gameButton.pack()
highScoreButton = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="white",
    fg="black",
)
highScoreButton.pack()

window.mainloop()
