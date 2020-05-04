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
        print("Clicked")
        button.place_forget()
        self.spawnNewButton()
        
    def spawnNewButton(self):
        print(self.counter)
        if self.counter < 10:
            self.place(x=random.randint(50,(screenW-50)),y=random.randint(50,(screenH-100)))
            self.counter=self.counter+1
        else:
            self.finish()

    def finish(self):
        print("You're done hoe")
        endTime= (time.time()-self.startTime)
        print(f'This is how long you took {endTime:.2f} seconds')
        
    


    

        


#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#


startTime=time.time()
print(startTime)
button=Button(window,10, 5, "red",0,startTime)  
print(button.counter)

       
