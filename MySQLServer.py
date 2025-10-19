import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Replace with your actual password
        )

        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as db_error:
                print(f"Error while creating database: {db_error}")
            finally:
                cursor.close()
                connection.close()

    except Error as conn_error:
        print(f"Error while connecting to MySQL: {conn_error}")

# Run the function
create_database()
