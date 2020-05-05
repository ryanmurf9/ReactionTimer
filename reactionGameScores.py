import pyautogui
import tkinter as tk

#Sorts out resolution
screenW, screenH = pyautogui.size()
resolution=str(screenW)+"x"+str(screenH)
window3 = tk.Tk()
window3.title("Reaction Game")
window3.geometry(resolution)
#

#class score(tk.Label):
#    def __init__(self)


userArray=['one','two','three','four','five','six','seven','eight','nine','ten']
scoreArray=['1','2','3','4','5','6','7','8','9','10']
dateArray=['1/1','1/2','1/3','1/4','1/5','1/6','1/7','1/8','1/9','1/10']
x=0
label = tk.Label(
    font=("Courier", 50),
    padx=100,
    pady=100,
    text="High Scores",
    foreground="black",  
    background="#f0f0f0"
)


label.pack()
counter=0
newx=(screenW/2)
newy=250
while counter <10:
    label1 = tk.Label(
        font=("Courier", 20),
        text=userArray[counter],
        foreground="black",  
        background="#f0f0f0",

        
    )
    label1.place(x=newx-100,y=newy)
    label2 = tk.Label(
        font=("Courier", 20),
        text=scoreArray[counter],
        foreground="black",  
        background="#f0f0f0",
        
    )
    label2.place(x=newx,y=newy)
    label3 = tk.Label(
        font=("Courier", 20),
        text=dateArray[counter],
        foreground="black",  
        background="#f0f0f0",
        
    )
    label3.place(x=newx+100,y=newy)
    newy=newy+50
    counter=counter+1



