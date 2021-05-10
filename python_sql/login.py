import sqlite3

def datas():
    connection = sqlite3.connect("users.db") 
    cursor =  connection.cursor()
    # cursor.execute("CREATE TABLE users (name TEXT ,text TEXT)")

    # users = [
    #     ("ar.rahman","music"),
    #     ("atlee","filem"),
    #     ("ajith","bike"),
    # ]
    # cursor.executemany("INSERT INTO users VALUES (?,?)",users )

    cursor.execute("SELECT * FROM users")
    relust = cursor.fetchall()
    connection.commit()
    connection.close()
    return relust

db = datas()
out = "invalid username or password"
pas = input("Enter password :")
for x in db:
    if x[1] == pas:
        out = f"wellcome {x[0]}"
print(out)