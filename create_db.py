
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students(
id INTEGER PRIMARY KEY,
name TEXT,
branch TEXT,
marks INTEGER
)
""")

data = [
(1,"Angad Saha","ECSE",85),
(2,"Monoranjan Thakur","ECE",78),
(3,"Somorjit Kormokar","ECSE",90),
(4,"SK Sourodipto","ECE",70),
(5,"Partho Roy","ECSE",88)
]

cursor.executemany("INSERT INTO students VALUES (?,?,?,?)",data)

conn.commit()
conn.close()

print("Database created successfully")
