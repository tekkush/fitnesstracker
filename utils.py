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
    return True

def validate_fitness(calories,carbs,protein,fats):
    if calories<0 or carbs<0 or protein<0 or fats<0:
        return False
    
def validate_strings(s):
    """
    the function takes a string and checks if the string is non empty
    """
    if len(s) == 0:
        return False

def add_fitness(username,day,month,year,calories,carbs,protein,fats):
    """
    function takes the username , date information and fitness information and tries to add the information to fitness table in fitness_db. 
    function returns true if adding is successful and false if not
    a date object is made if the date object is invalid then False is returned
    if the fitness information is invalid i.e. a number less than zero then False is returned 
    """
    try:
        date = datetime.date(year,month,day)
        if not validate_fitness(calories,protein,fats):
            return False
        fitness_db.add_fitness(username,date,calories,carbs,protein,fats)
        return True
    except ValueError:
        print("incorrect date type")
        return False
    


def add_workout(username,date,exercise,sets,reps):
    """
    function takes the parameters required to add a record in workouts table in workout.db and validates them
    returns a boolean variable success depending on if adding the new record was successful or not depending on correct user input data type
    """
    success = True 
    while not validate_workout(exercise,sets,reps):
        print("enter a valid exercise name and sets & reps scheme")
        exercise = input("exercise name: ")
        try:
            sets = int(input("enter number of sets for this exercise: "))
            reps = int(input("enter number of reps for this exercise: "))
        except ValueError:
            success = False
            return success
    workout.add_record(username,date,exercise,sets,reps)
    return success

def print_options(options):
    print(options)
    option = input("enter an option")
    while not validate_strings(options):
        option = input("please enter a valid option included in the list above: ")
    return option
