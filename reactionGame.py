

#Used to create the SQL Database; only used once
def tableCreator():
    connection = sqlite3.connect("highScores.sqlite")
    crsr = connection.cursor()
    tableMaker = """CREATE TABLE scoreTable(user TEXT score TEXT date DATETIME);"""
    crsr.execute(tableMaker)
    connection.close()

#Adds score to SQL Database if it is high enough
def addHighScore(user, score):
    connection = sqlite3.connect("highScores.sqlite")
    crsr = connection.cursor()

    #Figuring out the lowest score (INCOMPLETE)
    crsr.execute("SELECT score FROM scoreTable")
    scoreArray = crsr.fetchall()
    print(scoreArray)
    print(type(scoreArray[1]))


    #Inserting new score and deleting old score
   # if score < lowScore:
    #    now = datetime.now()
     #   formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
      #  crsr.execute("INSERT into scoreTable values(?, ?, ?)", (score, user, formatted_date,))
      #  crsr.execute("DELETE from scoreTable where score = '?'", (lowscore,))"""


text=pyautogui.size()


#Change resolution from pyautogui format to tKinter format
def resolution():
    text=str(pyautogui.size())
    size= re.sub(r'''(Size)|width=|,|height=|([()])''',"",text)
    size=size.split()
    resolution=size[0] +"x"+ size[1]
    return[resolution]



window = tk.Tk()
window.geometry(resolution())
#Must be in window.geometry("500x500") format


entry = tk.Entry(
    font=("Courier", 30),
    fg="black",
    bg="#f0f0f0",
    width=50
)
entry.insert(0, "Username")
entry.pack()

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
    text="To Go To Game",
    width=25,
    height=5,
    foreground="black",
    background="#f0f0f0"
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
    background="#f0f0f0"
)
highScoreButton.pack()

window.mainloop()
