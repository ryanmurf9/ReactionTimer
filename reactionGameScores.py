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
        self.labels=[]
        self.backButton()
        self.labelPack()
    def setArrays(self, a, b, c):
        self.userArray = a
        self.scoreArray = b
        self.dateArray = c

    def createScreen(self):
        self.counter=0
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
            self.labels.append([label1,label2,label3])
    def clickedBack(self):
        self.counter=0
        while self.counter < len(self.userArray):
            self.labels[self.counter][0].place_forget()
            self.labels[self.counter][1].place_forget()
            self.labels[self.counter][2].place_forget()
            self.counter=self.counter+1
        self.backButton.place_forget()
        import reactionGameMenu
        self.label.pack_forget()
    def labelPack(self):
        self.label = tk.Label(
            font=("Courier", 50),
            padx=100,
            pady=100,
            text="High Scores",
            foreground="black",
            background="#f0f0f0"
        )
        self.label.pack()
    def backButton(self):
        self.backButton=tk.Button(
            font=("Courier", 30),
            text="GoBack",
            width=25,
            height=5,
            foreground="black",  
            background="#f0f0f0",
            command=self.clickedBack
        )
        self.backButton.place(x=(screenW/2),y=(screenH-200))
#Creates the title of the page

#
userArray=['one','two','three','four','five','six','seven','eight','nine','ten']
scoreArray=['1','2','3','4','5','6','7','8','9','10']
dateArray=['1/1','1/2','1/3','1/4','1/5','1/6','1/7','1/8','1/9','1/10']



#Creates the score screen
score=score()

score.setArrays(userArray,scoreArray,dateArray)
score.createScreen()
#


















