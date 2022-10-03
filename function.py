import sqlite3

# Creating DataBase
connection = sqlite3.connect("Hotel_Management_System.db")

class DatabaseConnector:

    def __init__(self):
        pass

    # This Method creates the table for the users
    def create_table():
        with connection:
            connection.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER NOT NULL, name TEXT, email TEXT, number TEXT, address TEXT, room_no TEXT, PRIMARY KEY (ID AUTOINCREMENT))")

    # This Method insert our Data to DataBase
    def submit(name, email, number, address, room_no):
        with connection:
            connection.execute("INSERT INTO users(name, email, number, address, room_no) VALUES(?,?,?,?,?)", (name, email, number, address, room_no))

    # This Method displays all our guest base on room number
    def display_guest(room_no):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE room_no = ?", (room_no))
        records = cursor.fetchall()
        return records

    # This Method displays all available guest Note(it displays only their names and room number)
    # its automatically called when a user check's in
    def display_all_guest():
        cursor = connection.cursor()
        cursor.execute("SELECT name, room_no FROM users")
        result = cursor.fetchall()
        return result

    # This Method commit our query
    def commit_connection():
        connection.commit()

    # This Method check out guest base on room number
    # its deletes the guest record
    def check_out(room_no):
        with connection:
            connection.execute("DELETE FROM users WHERE room_no = ?", (room_no,))
            # connection.commit()

        