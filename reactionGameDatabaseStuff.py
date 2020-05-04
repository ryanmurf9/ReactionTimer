import tkinter
import sqlite3
from datetime import datetime

#Used to create the SQL Database; only used once
def tableCreator():
    connection = sqlite3.connect("highScores.sqlite")
    crsr = connection.cursor()
    tableMaker = """CREATE TABLE scoreTable(user TEXT, score FLOAT, date DATETIME);"""
    crsr.execute(tableMaker)
    connection.close()

#Adds score to SQL Database if it is high enough
def checkAddHighScore(user, score):
    connection = sqlite3.connect("highScores.sqlite")
    crsr = connection.cursor()

    #Figuring out the lowest score (INCOMPLETE)
    crsr.execute("SELECT score FROM scoreTable")
    scoreArray = crsr.fetchall()
    lowScore = 0
    for x in scoreArray:
        if x[0] > lowScore:
            lowScore = x[0]
    
     #Option if score qualifies and the list is full
    if score < lowScore and len(scoreArray) == 10:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        crsr.execute("INSERT into scoreTable values(?, ?, ?)", (user, score, formatted_date,))
        
        crsr.execute("DELETE from scoreTable where score = '%d'" % (lowScore))
    #Option if scoreTable is not yet 
    elif len(scoreArray) < 10:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        crsr.execute("INSERT into scoreTable values(?, ?, ?)", (user, score, formatted_date,))

    connection.commit()
    connection.close()


checkAddHighScore("user7", 198)

