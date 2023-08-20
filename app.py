import database
import fitness_db
import sqlite3
import hashlib
import datetime



def validate_pass(password):
    special = ['$','#','&','^','%']
    if len(password)<8 or len(password) > 20:
        print("password must be of length greater than 8 and not exceeding 20 characters")
        return False
    if not any(char.isdigit() for char in password):
        print("Password should have atleast one numeral")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain atleast one uppercase letter")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain atleast one lower case character")
        return False
    if not any(char in special for char in password):
        print("Password must contain atleast one special character")
        return False
    return True

def register(username,password):
    while database.username_exists(username):
        print(f"username: {username} already taken")
        username = input("please type in another username: ")
    while not validate_pass(password):
        password = input("please input a valid password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    database.add_user(username,hashed_password)

def login(username,password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    logged_in = False
    if database.auth(username,hashed_password):
        return True
    return False

def validate_workout(exercise,sets,reps):
    if len(exercise) == 0 or sets<0 or reps<0:
        return False
    return True
       
    
def validate_strings(s):
    """
    
    """
    if len(s) == 0:
        return False

def add_workout(exercise,sets,reps):
    while not validate_workout(exercise,sets,reps):
        print("enter a valid exercise name and sets & reps scheme")
        exercise = input("exercise name: ")

        

