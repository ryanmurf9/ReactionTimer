import pyautogui
import tkinter as tk

screenW, screenH = pyautogui.size()


resolution=str(screenW)+"x"+str(screenH)

window = tk.Tk()
window.title("Reaction Game")
window.geometry(resolution)
#Must be in window.geometry("500x500") format
import reactionGameMenu


state='menu'
running=True
window.mainloop()
'''
while running:
    if state=='menu':
        import reactionGameMenu
    if state=='score':
        import reactionGameScore
    if state=='game':
        import reactionGameGame
#Kill program
'''

