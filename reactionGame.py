import pyautogui
import tkinter as tk
import sqlite3
import re

screenW, screenH = pyautogui.size()


text=pyautogui.size()


#Change resolution from pyautogui format to tKinter format
def resolution():
    text=str(pyautogui.size())
    size= re.sub(r'''(Size)|width=|,|height=|([()])''',"",text)
    size=size.split()
    resolution=size[0] +"x"+ size[1]
    return[resolution]



window = tk.Tk()
window.geometry(resolution())
#Must be in window.geometry("500x500") format


entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.insert(0, "Username")
entry.pack()

label = tk.Label(
    padx=100,
    pady=100,
    text="Reaction Test",
    foreground="black",  
    background="#f0f0f0"
)
label.pack()
gameButton = tk.Button(
    padx=100,
    pady=100,
    text="To Go To Game",
    width=25,
    height=5,
    foreground="black",  
    background="#f0f0f0"
)
gameButton.pack()
highScoreButton = tk.Button(
    padx=100,
    pady=100,
    text="High Scores",
    width=25,
    height=5,
    foreground="black",  
    background="#f0f0f0"
)
highScoreButton.pack()

window.mainloop()
