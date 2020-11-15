import sqlite3 as sql

class db_store:
    
    def __init__(self):
        self.conn = sql.connect("data.sqlite")
        self.sql_create_customers_table = """ 
            CREATE TABLE IF NOT EXISTS Customers (
                c_id integer PRIMARY KEY,
                name text,
                phoneNumber text
            ); """
        self.init_database()

    def __del__(self):
        conn.close()

    def init_database(self):
        c = self.conn.cursor()
        c.execute(self.sql_create_customers_table)
