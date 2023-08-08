import sqlite3
import database
import datetime

def create_table():
    # create a table if one does not exist already
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS fitness (username TEXT,date DATE,calories INT,weight REAL)")
    conn.commit
    conn.close

def add_record(username,date,calories,weight):
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO fitness VALUES (?,?,?,?)",(username,date,calories,weight))
    conn.commit()
    conn.close()

def average_weight(username,days):
    # calculates a users average weight over the given parameter days

    total = 0
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM fitness WHERE username=? ORDER BY id DESC LIMIT ?", (username,days))
    result = curr.fetchall()
    if result:
        for record in result:
           total += record[4]
        return (total/days)
    else:
        return -1
    
def average_calories(username,days):
    total = 0
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM fitness WHERE username=? ORDER BY id DESC LIMIT ?", (username,days))
    result = curr.fetchall()
    if result:
        for record in result:
           total += record[3]
        return (total/days)
    else:
        return -1