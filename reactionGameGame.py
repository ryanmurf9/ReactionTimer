import pyautogui
import tkinter as tk
import sqlite3
import time
import random


class Button(tk.Button):
    def __init__(self,window22,width,height,background,counter,startTime):
        super().__init__(window2,width=width,height=height,background=background,command=self.clicked)
        self.startTime=startTime
        self.counter=counter
        self.spawnNewButton()
       
        
    def clicked(self):
        print("Clicked")
        button.place_forget()
        self.spawnNewButton()
        
    def spawnNewButton(self):
        print(self.counter)
        if self.counter < 10:
            self.place(x=random.randint(50,(screenW-50)),y=random.randint(100,(screenH-200)))
            self.counter=self.counter+1
        else:
            self.finish()

    def finish(self):
        print("You're done hoe")
        endTime= (time.time()-self.startTime)
        print(f'This is how long you took {endTime:.2f} seconds')
        label = tk.Label(
            font=("Courier", 30),
            padx=100,
            pady=100,
            text=(f'This is how long you took {endTime:.2f} seconds'),
            foreground="black",  
            background="#f0f0f0"
        )
        label.pack()
    


    

        


#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
window2 = tk.Tk()
window2.title("Reaction Game")
window2.geometry(resolution)
#


startTime=time.time()
print(startTime)
button=Button(window2,10, 5, "red",0,startTime)  
print(button.counter)


