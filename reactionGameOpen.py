import pyautogui
import tkinter as tk

screenW, screenH = pyautogui.size()


resolution=str(screenW)+"x"+str(screenH)

window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#Must be in window.geometry("500x500") format
import reactionGameMenu
window.mainloop()
'''
running=True
while running:
    if state=menu:

    if state=score:

    if state=game:

Kill program
'''
