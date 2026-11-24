import psycopg2
import os 
connection = None
cursor = None

# Custom function for clearing the screen, keeps program nice and clean
def clear_screen():
    os.system('cls')

# Basic boiler plate code for opening a connection to the database
def open_conn():
    global connection, cursor
    # Opening the connection
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="healthmanagementsystem",
        user="postgres",
        password="postgres"
    )
    # Cursor object for doing operations in the database
    cursor = connection.cursor()

# Basic functionality for closing the connection and cleaning up the program
def close_conn():
    global connection, cursor

    #close the connections 
    cursor.close()
    connection.close()