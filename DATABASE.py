import sqlite3
conn = sqlite3.connect("hiit.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE         
 )
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS COURSES(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS COURSES(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES COURSES(id)  
)
""")

conn.comit()