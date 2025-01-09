import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
print("database created")


cursor.execute("CREATE TABLE student(studid INTEGER PRIMARY KEY AUTOINCREMENT,firstname TEXT ,lastname text, age INTEGER,email text )")

print("table created")


