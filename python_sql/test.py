import sqlite3
conn =  sqlite3.connect("database.db")

c = conn.cursor()
# c.execute("CREATE TABLE friends (name TEXT ,age INTEGER)")

# people =[
#     ("a",1),
#     ("b",2),
#     ("c",32),
#     ("d",4),]
# qur = "INSERT INTO friends VALUES (?,?)"
# c.executemany(qur,people)
# c.execute("select * from friends")
# print(c.fetchall())

conn.commit()
conn.close()

