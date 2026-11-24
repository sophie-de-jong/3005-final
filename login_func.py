import conn_func
def login():
    # fname = input("Enter first name: ")
    # lname = input("Enter last name: ")

    conn_func.cursor.execute("SELECT * FROM Member;")
    print(conn_func.cursor.fetchall())
