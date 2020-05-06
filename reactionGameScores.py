import pyautogui
import tkinter as tk

#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
window3 = tk.Tk()
window3.title("Reaction Game")
window3.geometry(resolution)
#


class score(tk.Label):
    self.userArray=['one','two','three','four','five','six','seven','eight','nine','ten']
    self.scoreArray=['1','2','3','4','5','6','7','8','9','10']
    self.dateArray=['1/1','1/2','1/3','1/4','1/5','1/6','1/7','1/8','1/9','1/10']
    def __init__(self):
        self.newx=(screenW/2)
        self.newy=250
        self.counter=0
    def createScreen(self):
        while self.counter <10:
            label1 = tk.Label(
                font=("Courier", 20),
                text=userArray[self.counter],
                foreground="black",
                background="#f0f0f0",
            )

            label1.place(x=self.newx-100,y=self.newy)
            label2 = tk.Label(
                font=("Courier", 20),
                text=scoreArray[self.counter],
                foreground="black",
                background="#f0f0f0",

            )
            label2.place(x=self.newx,y=self.newy)
            label3 = tk.Label(
                font=("Courier", 20),
                text=dateArray[self.counter],
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
