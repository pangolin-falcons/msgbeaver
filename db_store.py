import sqlite3 as sql
import csv

class db_store:
    
    def __init__(self):
        self.conn = sql.connect("data.sqlite")
        self.sql_create_customers_table = """ 
            CREATE TABLE IF NOT EXISTS Customers (
                c_id integer PRIMARY KEY,
                name text,
                phoneNumber text
            ); """
        self.sql_create_vendors_table = """ 
            CREATE TABLE IF NOT EXISTS Vendors (
                v_id integer PRIMARY KEY,
                name text,
                phoneNumber text,
                keyword text
            ); """
        self.sql_create_orders_table = """ 
            CREATE TABLE IF NOT EXISTS Orders (
                o_id integer PRIMARY KEY,
                v_id integer,
                c_id integer,
                request text,
                is_accepted integer DEFAULT 0,
                is_complete integer DEFAULT 0,
                phoneNumber text,
                FOREIGN KEY(v_id) REFERENCES Vendors,
                FOREIGN KEY(c_id) REFERENCES Customers
            ); """
        self.sql_create_messages_table = """ 
            CREATE TABLE IF NOT EXISTS Messages (
                m_id integer PRIMARY KEY,
                o_id,
                v_id integer,
                c_id integer,
                messageBody text,
                phoneNumber text,
                FOREIGN KEY(o_id) REFERENCES Orders,
                FOREIGN KEY(v_id) REFERENCES Vendors,
                FOREIGN KEY(c_id) REFERENCES Customers
            ); """
        self.init_database()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def init_database(self):
        c = self.conn.cursor()
        c.execute(self.sql_create_customers_table)
        c.execute(self.sql_create_vendors_table)
        c.execute(self.sql_create_orders_table)
        c.execute(self.sql_create_messages_table)

    def load_db(self):
        c = self.conn.cursor()
        with open('dataload/customers.csv', 'r') as f:
            data = csv.DictReader(f)
            dbReady = [(i['c_id'], i['name'], i['phoneNumber']) for i in data]
        c.executemany("INSERT INTO Customers (c_id, name, phoneNumber) VALUES (?, ?, ?);", dbReady)
        self.conn.commit()
        with open('dataload/vendors.csv', 'r') as f:
            data = csv.DictReader(f)
            dbReady = [(i['v_id'], i['name'], i['phoneNumber'], i['keyword']) for i in data]
        c.executemany("INSERT INTO Vendors (v_id, name, phoneNumber, keyword) VALUES (?, ?, ?, ?);", dbReady)
        self.conn.commit()
        c = self.conn.cursor()
        with open('dataload/orders.csv', 'r') as f:
            data = csv.DictReader(f)
            dbReady = [(i['o_id'], i['v_id'], i['c_id'], i['request'], 
                       i['is_accepted'], i['is_complete']) for i in data]
        c.executemany("""INSERT INTO Orders (o_id, v_id, c_id, request, is_accepted, is_complete) 
                           VALUES (?, ?, ?, ?, ?, ?);""", dbReady)
