import pyautogui
import tkinter as tk
import sqlite3


screenW, screenH = pyautogui.size()
print(screenW)
print(screenH)



resolution=str(screenW)+"x"+str(screenH)

window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#Must be in window.geometry("500x500") format


entry = tk.Entry(
    font=("Courier", 30),
    fg="black",
    bg="#f0f0f0",
    width=50
)
entry.insert(0, "Username")
entry.pack()

label = tk.Label(
    font=("Courier", 30),
    padx=100,
    pady=100,
    text="Reaction Test",
    foreground="black",  
    background="#f0f0f0"
)
label.pack()
gameButton = tk.Button(
    font=("Courier", 30),
    padx=100,
    pady=50,
    text="To Go To Game",
    width=25,
    height=5,
    foreground="black",  
    background="#f0f0f0"
)
gameButton.pack()
highScoreButton = tk.Button(
    font=("Courier", 30),
    padx=100,
    pady=50,
    text="High Scores",
    width=25,
    height=5,
    foreground="black",  
    background="#f0f0f0"
)
highScoreButton.pack()

window.mainloop()
