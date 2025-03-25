import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DataBase():
    def __init__(self):
        self._conn = None
        self._cursor = None

    
    def __enter__(self):
        self._conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="user_intro"
        )
        try:
            self._cursor = self._conn.cursor()
            return self
        except mysql.connector.Error as e:
            print(f"Error while connection to MYSQL {e}")

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._cursor:
            self._cursor.close()
        
        if self._conn:
            if exc_type is None:
                self._conn.commit()
            else:
                self._conn.rollback()
        self._conn.close()
    
    @property
    def conn(self):
        return self._conn
    
    @property
    def cursor(self):
        return self._cursor
    
    def load_user(self, user_id):
        self._cursor.execute("SELECT * FROM users WHERE id = %s", (user_id, ))
        return self._cursor.fetchone()
    
    def create_user(self, name, email, password):
        self._cursor.execute("INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, 'user')", (name, email, password))
        # Default role set to 'user'
        return 
    
    def load_user_by_email(self, email):
        self._cursor.execute("SELECT * FROM users WHERE email = %s", (email, ))
        return self._cursor.fetchone()