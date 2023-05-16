import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(":memory:") # create a memory-based temporary database for demo
        print(f'successful connection to sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_connection()