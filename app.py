import database
import fitness_db
import sqlite3
import hashlib
import datetime




def register(username,password):
    while database.if_exists(username):
        print(f"username: {username} already taken")
        username = input("please type in another username: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    database.add_user(username,hashed_password)

def login(username,password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    logged_in = False
    if database.auth(username,hashed_password):
        return True
    return False

def log(username,calories,weight):
    current_date = datetime.now().date()
    fitness_db.add_record(username,current_date,calories,weight)


database.create_table()
mock_data = [
    {"username": "alice", "password": "secretpassword"},
    {"username": "bob", "password": "bobspassword"},
    {"username": "charlie", "password": "charliespassword"},
    # Add more mock user data here
]
for data in mock_data:
    register(data["username"],data["password"])
database.show_all()
