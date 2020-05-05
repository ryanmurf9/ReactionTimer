import pyautogui
import tkinter as tk
import sqlite3


screenW, screenH = pyautogui.size()


resolution=str(screenW)+"x"+str(screenH)

window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#Must be in window.geometry("500x500") format
#When the game button is clicked it opens the game 
def clickedGame():
    import reactionGameGame
    label.pack_forget()
    gameButton.pack_forget()
    highScoreButton.pack_forget()
#
#When High scores are clicked it opens high scores
def clickedScore():
    import reactionGameScores
    label.pack_forget()
    gameButton.pack_forget()
    highScoreButton.pack_forget()
#
#Buttons and Title
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
    text="Play Game",
    width=25,
    height=5,
    foreground="black",  
    background="#f0f0f0",
    command=clickedGame
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
    background="#f0f0f0",
    command=clickedScore
    
)
highScoreButton.pack()
###
window.mainloop()
