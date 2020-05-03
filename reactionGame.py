import tkinter
import sqlite3
from datetime import datetime


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

addHighScore("user3", 5)
