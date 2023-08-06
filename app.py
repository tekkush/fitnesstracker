import database
import sqlite3
import hashlib

database.create_table()

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
    while database.if_exists(username):
        print(f"username: {username} already taken")
        username = input("please type in another username: ")
    while not validate_pass(password):
        password = input("please input a valid password: ")
    hashed_password = hashlib.sha256(password)
    database.add_user(username,password)