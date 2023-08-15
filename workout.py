import sqlite3
from datetime import datetime


def create_table():
    # create a table if one does not exist already
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS workouts (username TEXT,date DATE,exercise TEXT,sets INT,reps INT)")
    conn.commit()
    conn.close()


def add_record(username,date,exercise,sets,reps):
    current_date = datetime.now().date()
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO workouts VALUES (?,?,?,?)" (username,exercise,sets,reps))
    conn.commit()
    conn.close()

def return_workout(username,date):
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM workouts WHERE username=? AND date=?",(username,date))
    result = curr.fetchall()
    return result

def update_workout(username,date)

