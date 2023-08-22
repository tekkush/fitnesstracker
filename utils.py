import database
import workout
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
    while len(username) == 0:
        username = input("enter a non-empty username: ")
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
    try:
        sets = int(input("enter number of sets for this exercise: "))
        reps = int(input("enter number of reps for this exercise: "))
    except ValueError:
        print("please use only integer/whole number inputs for reps and sets")
        return False
    return True

def validate_fitness(day,month,year,calories,carbs,protein,fats):
    date = create_date(year,month,day)
    if date == -1:
        return False
    if calories
    
def validate_strings(s):
    """
    the function takes a string and checks if the string is non empty
    """
    if len(s) == 0:
        return False
def create_date(day,month,year):
    """
    function takes the day,month and year for a particular date 
    if the date is invalid -1 is returned
    """
    try:
        date = datetime.date(year,month,day)
    except ValueError:
        return -1
    return date

def add_workout(exercise,sets,reps):
    """
    function takes the parameters required to add a record in workouts table in workout.db and validates them
    """
    while not validate_workout(exercise,sets,reps):
        print("enter a valid exercise name and sets & reps scheme")
        exercise = input("exercise name: ")
        sets = int(input("enter number of sets for this exercise: "))
        reps = int(input("enter number of reps for this exercise: "))
    workout.add_record(exercise,sets,reps)

def print_options(options):
    print(options)
    option = input("enter an option")
    while not validate_strings(options):
        option = input("please enter a valid option included in the list above: ")
    return option
