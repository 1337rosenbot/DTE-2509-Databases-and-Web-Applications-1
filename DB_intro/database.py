# pip install mysql-connector-python
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class DataBase():
    def __init__(self):
        self.mysqlConnection = None
        self.cursor = None
        
    
    def __enter__(self):
        self.mysqlConnection = mysql.connector.connect(
            host="localhost", #port 3306
            user="flaskproject",
            password=os.getenv("DB_PASSWORD"),
            database="db_info"
        )
        try:
            self.cursor = self.mysqlConnection.cursor()
            return self
        except mysql.connector.Error as error:
            print(f"Error while connecting to MYSql: {error}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.mysqlConnection:
            if exc_type is None:
                self.mysqlConnection.commit()  # commit only if no exception
            else:
                self.mysqlConnection.rollback()  # rollback if an exception occurred
            self.mysqlConnection.close()

    def getAllData(self):
        self.cursor.execute("SELECT * FROM film;")
        return self.cursor.fetchall()
    
    def getMovieById(self, movie_id):
        self.cursor.execute("SELECT * FROM film WHERE fnr= %s", (movie_id, )) # Note that the single parameter is made as a tuple
        return self.cursor.fetchone()
    
    # Preventing  SQL Injection (Prepared Statements)
    # Ensuring the right data structure
    # Consistency with multiple parameters (making the "connector"-api more predictable)


    def create_movie(self, data):
        sql = """
            INSERT INTO film (tittel, år, land, sjanger, alder, tid, pris)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        self.cursor.execute(sql, data)
        return self.cursor.fetchone()
    