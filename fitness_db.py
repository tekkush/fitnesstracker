import sqlite3
import database
from datetime import datetime,timedelta


def create_table():
    # create a table if one does not exist already
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS fitness (username TEXT,date DATE,calories INT,carbs INT,protein INT,fats INT,weight REAL)")
    conn.commit()
    conn.close()

def add_record(username,date,calories,carbs,protein,fats,weight):
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO fitness VALUES (?,?,?,?,?,?,?)",(username,date,calories,carbs,protein,fats,weight))
    conn.commit()
    conn.close()

def return_total(username,date):
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM fitness WHERE username=? AND date=?", (username,date))
    result = curr.fetchall()
    conn.close()
    total_cal = 0
    total_carb = 0
    total_protein = 0
    total_fat = 0
    for record in result:
        total_cal += record[3]
        total_carb += record[4]
        total_protein += record[5]
        total_fat += record[6]
    return([total_cal,total_carb,total_protein,total_fat])
    



def average_weight(username,days):
    # calculates a users average weight over the given parameter days

    totals = [] #storing the total for each day 
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
    totals = [] #storing total calories for each day
    current_date = datetime.now().date()
    end_date = current_date
    start_date = current_date - timedelta(days=days - 1)

    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT SUM(calories) FROM fitness WHERE username=? AND date BETWEEN ? AND ?", (username,start_date,end_date))
    sum_calories = curr.fetchone()[0]

    curr.execute("SELECT COUNT(calories) FROM fitness WHERE username=? AND date BETWEEN ? AND ?",(username,start_date,end_date))
    records = curr.fetchone()[0]
    if records == 0:
        return -1
    conn.commit()
    conn.close()
    average_calories = sum_calories/records
    return average_calories
