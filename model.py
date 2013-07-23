"""
model.py
"""
import sqlite3
import re

from datetime import datetime

DB = None
CONN = None

def connect_db():
    return sqlite3.connect("tipsy.db")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    name = Column(String(64), nullable=True)

    def new_user(email, password, name):          
    c = db.cursor()                                     
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    c.execute(query, (email, password, name))           
    db.commit()

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

    return None

def get_user(db, user_id):
    """Gets a user dictionary out of the database given an id"""
    pass

def new_task(title, datestamp, user_id):
    query = """INSERT into Tasks values (?,?,?)"""
    DB.execute(query, (title, datetime.now(), user_id))
    CONN.commit()
    return "Successfully added task: %s" % title

def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    pass

def get_tasks(db, user_id=None):
    """Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
    pass

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("tipsy.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None

if __name__ == "__main__":
    main()