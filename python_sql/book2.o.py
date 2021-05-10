import sqlite3

def data():
    connection  = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data

for x in data():
    print(x[0])
