import sqlite3
from datetime import datetime

"""
Database script for workouts functionalities include:
creation of table with fields: "username" "date" "exercise" "sets" "reps"
returning the records/exercises and sets & reps for a specific user on a given day can be retrieved 
an exercise can be added
exercises can be modified/deleted in terms of exercise,sets and reps
"""

def create_table():
    # create a table if one does not exist already
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS workouts (username TEXT,date DATE,exercise TEXT,sets INT,reps INT)")
    conn.commit()
    conn.close()


def add_record(username,date,exercise,sets,reps):
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO workouts VALUES (?,?,?,?,?)" (username,date,exercise,sets,reps))
    conn.commit()
    conn.close()

def return_workout(username,date):
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM workouts WHERE username=? AND date=?",(username,date))
    result = curr.fetchall()
    return result

def delete_workout(username,date,exercise):
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()

    curr.execute("DELETE FROM workouts WHERE username=? AND date=? AND exercise=?",(username,date,exercise))
    conn.commit()
    conn.close()

def update_workout(username,date,exercise,sets,reps):
    delete_workout(username,date,exercise)
    add_record(username,exercise,sets,reps)

def show_all():
    conn = sqlite3.connect("workout.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM workouts")
    records = curr.fetchall()
    for record in records:
        print(records)
    conn.commit()
    conn.close()