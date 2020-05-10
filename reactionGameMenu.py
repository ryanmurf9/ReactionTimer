import pyautogui
import tkinter as tk
import sqlite3

print('yeet this meat')

#Must be in window.geometry("500x500") format
#When the game button is clicked it opens the game 
def clickedGame():
    gameButton.pack_forget()
    highScoreButton.pack_forget()
    label.pack_forget()
    import reactionGameGame
    
    
#
#When High scores are clicked it opens high scores
def clickedScore():
    label.pack_forget()
    gameButton.pack_forget()
    highScoreButton.pack_forget()
    import reactionGameScores
    
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
print('yeet this meat2')
###
##window.mainloop()
