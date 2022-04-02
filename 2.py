import sqlite3

db = sqlite3.connect("morty.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dogs
(
    name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL,
    colour VARCHAR(32) NOT NULL
)
""")

dogs = [('doggo', 1, 'black'), ('doggo2', 2, 'brown')]
cursor.executemany("INSERT INTO dogs (name, age, colour) VALUES (?, ?, ?)", dogs)

db.commit()
db.close()