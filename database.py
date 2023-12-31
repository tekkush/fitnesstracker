import sqlite3

"""
Database script for:
storing user authentication info
authenticating users 
viewing all user authentication info
"""

def create_table():
    # create a table if one does not exist already
    conn = sqlite3.connect("users.db")
    curr = conn.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY,password TEXT)")
    conn.commit()
    conn.close()

def show_all():
    """
    function show_all prints all records
    """
    conn = sqlite3.connect("users.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM users")
    records = curr.fetchall()
    for record in records:
        print(record)
    conn.commit()
    conn.close()

def add_user(username,hashed_pass):
    """
    
    """
    conn = sqlite3.connect("users.db")
    curr = conn.cursor()
    curr.execute("INSERT INTO users VALUES (?,?)", (username,hashed_pass))
    conn.commit()
    conn.close()

def username_exists(username):
    # check if a username is already taken
    conn = sqlite3.connect("users.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = curr.fetchone()
    if result:
        return True
    return False

def auth(username,hashed_pass):
    conn = sqlite3.connect("users.db")
    curr = conn.cursor()
    
    curr.execute("SELECT * FROM users WHERE username=? AND password",(username,hashed_pass))
    result = curr.fetchone()
    conn.close()
    
    if result:
        return True
    return False

def clear_table():
    conn = sqlite3.connect("users.db")
    curr = conn.cursor()

    curr.execute("DELETE FROM users")
    conn.commit()
    conn.close()