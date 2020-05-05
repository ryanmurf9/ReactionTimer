import pyautogui
import tkinter as tk
import sqlite3
import time
import random


class Button(tk.Button):
    def __init__(self,window,width,height,background,counter,startTime):
        super().__init__(window,width=width,height=height,background=background,command=self.clicked)
        self.startTime=startTime
        self.counter=counter
        self.spawnNewButton()
       
        
    def clicked(self):
        button.place_forget()
        self.spawnNewButton()
        
    def spawnNewButton(self):
        if self.counter < 10:
            self.place(x=random.randint(50,(screenW-50)),y=random.randint(100,(screenH-200)))
            self.counter=self.counter+1
        else:
            self.finish()

    def finish(self):
        endTime= (time.time()-self.startTime)
        print(f'Time: {endTime:.2f} seconds')
        label = tk.Label(
            font=("Courier", 30),
            padx=100,
            pady=100,
            text=(f'Time: {endTime:.2f} seconds'),
            foreground="black",  
            background="#f0f0f0"
        )
        label.pack()
        self.gameOver()

        
    def gameOver(self):
        gameOver= tk.Button(
            font=("Courier", 30),
            text=('Game Over'),
            foreground="black",  
            background="#f0f0f0"
        )
        gameOver.pack()


        


#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#


startTime=time.time()
button=Button(window,10, 5, "red",0,startTime)  



