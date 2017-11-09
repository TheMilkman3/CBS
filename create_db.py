import sqlite3 as sql


def create_db(db_name):
    with sql.connect(db_name) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE actors (id integer primary key, name text, image text,
        alignment text, location integer)''')
        c.executemany('''INSERT INTO actors (name, image, alignment, location) VALUES (?, ?, ? , ?)''',
                      (('Bob', 'N/A', 0, 0), ('Alice', 'N/A', 0, 0), ('Christine', 'N/A', 0, 0)))


create_db('database.db')
