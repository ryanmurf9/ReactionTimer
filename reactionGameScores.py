import pyautogui
import tkinter as tk

#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
#


class score(tk.Label):
    def __init__(self):
        self.newx=(screenW/2)
        self.newy=250
        self.counter=0
        self.userArray=[]
        self.scoreArray=[]
        self.dateArray=[]

    def setArrays(self, a, b, c):
        self.userArray = a
        self.scoreArray = b
        self.dateArray = c

    def createScreen(self):
        while self.counter < len(self.userArray):
            label1 = tk.Label(
                font=("Courier", 20),
                text=self.userArray[self.counter],
                foreground="black",
                background="#f0f0f0",
            )

            label1.place(x=self.newx-100,y=self.newy)
            label2 = tk.Label(
                font=("Courier", 20),
                text=self.scoreArray[self.counter],
                foreground="black",
                background="#f0f0f0",

            )
            label2.place(x=self.newx,y=self.newy)
            label3 = tk.Label(
                font=("Courier", 20),
                text=self.dateArray[self.counter],
                foreground="black",
                background="#f0f0f0",

            )
            label3.place(x=self.newx+100,y=self.newy)
            self.newy=self.newy+50
            self.counter=self.counter+1

#Creates the title of the page
label = tk.Label(
    font=("Courier", 50),
    padx=100,
    pady=100,
    text="High Scores",
    foreground="black",
    background="#f0f0f0"
)
label.pack()
#


#Creates the score screen
score=score()
score.createScreen()
#
