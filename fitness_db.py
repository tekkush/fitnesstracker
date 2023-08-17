import sqlite3
import database
from datetime import datetime,timedelta

"""
Database script for user fitness and health, functionalities include:
creation and deletion of fitness and user_health tables
adding user fitness data (calories,carbs,protein,fats)
retrieving averages for number of days for user fitness & health
"""

def create_table():
    # create a table if one does not exist already
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS fitness (username TEXT,date DATE,calories INT,carbs INT,protein INT,fats INT)")
    curr.execute("CREATE TABLE IF NOT EXISTS user_health (username TEXT,date DATE,weight REAL,sleep_hours REAL)")
    conn.commit()
    conn.close()

def add_fitness(username,date,calories,carbs,protein,fats):
    """
    
    """
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO fitness VALUES (?,?,?,?,?,?)",(username,date,calories,carbs,protein,fats))
    conn.commit()
    conn.close()

def add_health(username,date,weight,sleep_hours):
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO user_health VALUES (?,?,?,?)",(username,date,weight,sleep_hours))
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
     
def average_calories(username,days):
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

def average_carbs(username,days):
    if days == 0:
        return -2 
    current_date = datetime.now().date()
    end_date = current_date
    start_date = current_date - timedelta(days=days - 1)

    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT SUM(carbs) FROM fitness WHERE username=? AND date BETWEEN ? AND ?", (username,start_date,end_date))
    sum_carbs = curr.fetchone()[0]

    curr.execute("SELECT COUNT(carbs) FROM fitness WHERE username=? AND date BETWEEN ? AND ?",(username,start_date,end_date))
    records = curr.fetchone()[0]
    if records == 0:
        return -1
    conn.commit()
    conn.close()
    average_carbs = sum_carbs/records
    return average_carbs

def average_protein(username,days):
    current_date = datetime.now().date()
    end_date = current_date
    start_date = current_date - timedelta(days=days - 1)

    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT SUM(protein) FROM fitness WHERE username=? AND date BETWEEN ? AND ?", (username,start_date,end_date))
    sum_protein = curr.fetchone()[0]

    curr.execute("SELECT COUNT(protein) FROM fitness WHERE username=? AND date BETWEEN ? AND ?",(username,start_date,end_date))
    records = curr.fetchone()[0]
    if records == 0:
        return -1
    conn.commit()
    conn.close()
    average_protein = sum_protein/records
    return average_protein

def average_fats(username,days):
    current_date = datetime.now().date()
    end_date = current_date
    start_date = current_date - timedelta(days=days - 1)

    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT SUM(protein) FROM fitness WHERE username=? AND date BETWEEN ? AND ?", (username,start_date,end_date))
    sum_protein = curr.fetchone()[0]

    curr.execute("SELECT COUNT(protein) FROM fitness WHERE username=? AND date BETWEEN ? AND ?",(username,start_date,end_date))
    records = curr.fetchone()[0]
    if records == 0:
        return -1
    conn.commit()
    conn.close()
    average_protein = sum_protein/records
    return average_protein

def all_fitness_averages(username,days):
    return( [average_calories(username,days) , average_carbs(username,days) , average_protein(username,days), average_fats(username,days)] )

def return_weight(username,date):
    """
    function return_weight
    takes two parameters username (string) and date(date)
    returns user weight on the given date or -1 if no record for user_health can be found on that date
    """
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("SELECT weight FROM user_health WHERE username=? AND date=?",(username,date))
    result = curr.fetchone()
    if not result:
        return -1
    weight = result[0]
    return weight

def clear_table():
    conn = sqlite3.connect("fitness.db")
    curr = conn.cursor()

    curr.execute("DELETE FROM fitness")
    curr.execute("DELETE FROM user_health")
    conn.commit()
    conn.close()
