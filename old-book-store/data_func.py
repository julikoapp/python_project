import sqlite3


class Database:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.curs = self.conn.cursor()
        self.curs.execute(
            "CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def view_all_books(self):
        self.curs.execute("SELECT * FROM bookstore")
        rows = self.curs.fetchall()
        self.conn.commit()
        return rows

    def add_book(self, title, author, year, isbn):
        self.curs.execute("INSERT INTO bookstore VALUES(NULL, ?, ?,?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def find_book(self, name="", author="", year="", isbn=""):
        self.curs.execute("SELECT * FROM bookstore WHERE title=?OR author=? OR year=? or isbn=?",
                          (name, author, year, isbn))
        rows = self.curs.fetchall()
        self.conn.commit()
        return rows

    def delete_book(self, id):
        self.curs.execute("DELETE FROM bookstore WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.curs.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",
                          (id, title, author, year, isbn))
        self.conn.commit()

    def delete_table(self):
        self.curs.execute("DROP TABLE IF EXISTS bookstore")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
