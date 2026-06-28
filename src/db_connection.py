import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Admin@1234",
    "database": "trg_demo",
}

def get_connection(database: str = None):
    config = {**DB_CONFIG, **({"database": database} if database else {})}
    connection = mysql.connector.connect(**config)
    return connection

def execute_query(query: str, params: tuple = (), database: str = None):
    connection = get_connection(database)
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        connection.close()

def fetch_all(query: str, params: tuple = (), database: str = None):
    connection = get_connection(database)
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

def fetch_one(query: str, params: tuple = (), database: str = None):
    connection = get_connection(database)
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    try:
        conn = get_connection()
        print(f"Connected to MySQL server v{conn.get_server_info()}")
        conn.close()
    except Error as e:
        print(f"Connection failed: {e}")
