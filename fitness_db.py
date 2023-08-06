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
    pass
