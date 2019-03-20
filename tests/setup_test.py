import sqlite3
from app.orm import ORM

def schema():
    with sqlite3.connect("_example.db") as conn:
        cur = conn.cursor()
        SQL = "DROP TABLE IF EXISTS example;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE example (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            name VARCHAR(128),
            salary FLOAT); """
        cur.execute(SQL)

        SQL = """ INSERT INTO example(employee_id, name, salary)
                    VALUES(?, ?, ?); """

        cur.execute(SQL, (1, 'jack', 100.0))
        cur.execute(SQL, (2, 'jill', 200.0))

class Example(ORM):
    fields = ["employee_id", "name", "salary"]
    table = "example"
    database = "_example.db"

    def __init__(self):
        self.pk = None
        self.employee_id = None
        self.name = None
        self.salary = None
