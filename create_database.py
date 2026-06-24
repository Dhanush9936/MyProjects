import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")

students = [
    (1, "Rahul", 20, "A"),
    (2, "Priya", 21, "B"),
    (3, "Arjun", 19, "A"),
    (4, "Sneha", 20, "C")
]

cursor.executemany(
    "INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)",
    students
)

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
