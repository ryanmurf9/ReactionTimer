import tkinter
import sqlite3
from datetime import datetime

#Handles all database functions
class Database:
    #Creating Lists
    def __init__(self):
        self.userList = []
        self.scoreList = []
        self.dateList = []
        
    #Used to create the SQL Database; only used once
    def tableCreator(self):
        connection = sqlite3.connect("highScores.sqlite")
        crsr = connection.cursor()
        tableMaker = """CREATE TABLE scoreTable(user TEXT, score FLOAT, date DATETIME);"""
        crsr.execute(tableMaker)
        connection.close()

    #Adds score to SQL Database if it is high enough
    def checkAddHighScore(self, user, score):
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
        #Option if scoreTable is not yet full
        elif len(scoreArray) < 10:
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            crsr.execute("INSERT into scoreTable values(?, ?, ?)", (user, score, formatted_date,))

        #Saves andy changes that may have been made and closes the database connection
        connection.commit()
        connection.close()

    #Used to retrieve and formate the highscore table data
    def getScoreData(self):
        #Connecting to database and filling scoreArray with data
        connection = sqlite3.connect("highScores.sqlite")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM scoreTable ORDER BY score ASC")
        scoreArray = crsr.fetchall()
        for x in scoreArray:
            self.userList.append(x[0])
            self.scoreList.append(x[1])
            self.dateList.append(x[2])
            
            
        



