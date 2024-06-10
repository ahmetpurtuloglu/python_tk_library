import sqlite3

class LibraryManager:
    def __init__(self):
        self.conn = None
        self.cur = None

    @staticmethod
    def get_connection():
        return sqlite3.connect("library.db")

    def create_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
        create table if not exists Book (
            gid   integer primary key autoincrement,
            name text,
            page_number integer,
            short_description text,
            category text
        );
        """)
        self.cur.execute("""
        create table if not exists Librarian (
            gid   integer primary key autoincrement,
            name text,
            age integer,
            gender text
        );
        """)
        self.cur.execute("""
        create table if not exists Category (
            gid   integer primary key autoincrement,
            name text
        );
        """)
        self.conn.commit()
        self.conn.close()

    def fill_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        data = []

        for item in data:
            self.cur.execute("insert into Book(name, page_number, short_description, category) values(?, ?, ?, ?)", item)

        self.conn.commit()
        self.conn.close()

    def clear_book_from_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Book")
        self.conn.commit()
        self.conn.close()

    def clear_librarian_from_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Librarian")
        self.conn.commit()
        self.conn.close()    

    def clear_category_from_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Category")
        self.conn.commit()
        self.conn.close()        

    def add_book(self, name, page_number,short_description,category):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into Book(name, page_number, short_description, category) values(:name, :page_number, :short_description, :category)",
                    {"name": name,
                     "page_number": page_number,
                     "short_description": short_description,
                     "category": category})
        self.conn.commit()
        self.conn.close()

    def add_librarian(self, name,age,gender):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into Librarian(name, age, gender) values(:name, :age, :gender)",
                    {"name": name,
                     "age": age,
                     "gender": gender})
        self.conn.commit()
        self.conn.close()

    def add_category(self, name):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into Category(name) values(:name)",
                    {"name": name})
        self.conn.commit()
        self.conn.close()    

    def list_books(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from Book")
        books = self.cur.fetchall()
        self.conn.close()
        return books

    def list_librarians(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from Librarian")
        librarians = self.cur.fetchall()
        self.conn.close()
        return librarians  

    def list_categories(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from Category")
        categories = self.cur.fetchall()
        self.conn.close()
        return categories    

    def delete_book(self, gid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Book where gid=?", [gid])
        self.conn.commit()

    def delete_librarian(self, gid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Librarian where gid=?", [gid])
        self.conn.commit()

    def delete_category(self, gid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Category where gid=?", [gid])
        self.conn.commit()    

    def edit_book(self, gid, name, page_number,short_description, category):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update Book set name=?, page_number=?, short_description=?, category=? where gid=?",
                         [name, page_number, short_description,category, gid])
        self.conn.commit()

    def edit_librarian(self, gid, name, age, gender):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update Librarian set name=?, age=?, gender=? where gid=?",
                         [name, age, gender, gid])
        self.conn.commit()  

    def edit_category(self, gid, name):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update Category set name=? where gid=?",
                         [name,gid])
        self.conn.commit()  

    def get_categories(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from Category")
        categories = self.cur.fetchall()
        self.conn.close()
        return [category[1] for category in categories]            
