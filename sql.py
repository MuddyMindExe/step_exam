import sqlite3


class Files:
    @staticmethod
    def open_con(func):
        def wrap(table, *args):
            con = sqlite3.connect('bookstore.db')
            cursor = con.cursor()
            Files.init(cursor)
            func(table, cursor, *args)
            con.commit()
            con.close()

        return wrap

    @staticmethod
    @open_con
    def init(cursor):
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            phone INTEGER NOT NULL,
            mail TEXT NOT NULL
        )
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            buy_price INTEGER NOT NULL,
            sell_price INTEGER NOT NULL
        )
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS sells (
            employee_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            profit INTEGER NOT NULL
        )
        ''')

    @staticmethod
    def form_add_query(table: str):
        columns = {"employees": "(name, position, phone, mail)",
                   "books": "(name, year, author, genre, buy_price, sell_price)",
                   "sells": "(employee_phone, book_id, date, profit)"}
        placeholders = ', '.join(['?'] * (columns[table].count(',') + 1))
        query = f""" 
                    INSERT INTO {table} {columns[table]} Values ({placeholders})
                 """
        return query.strip()

    @staticmethod
    def form_delete_query(table: str, columns: dict):
        where = " AND ".join([f'{column} = ?' for column in columns.keys()])
        query = f""" 
                    DELETE FROM {table} WHERE {where}
                 """
        return query.strip()

    @staticmethod
    def duplicate(table, *args):
        all_data = Files.return_all(table)
        wanted_column = tuple([_ for _ in args])
        return wanted_column in all_data

    @staticmethod
    @open_con
    def add_info(table: str, args, cursor):
        try:
            query = Files.form_add_query(table)
            cursor.execute(query, tuple(args))
            return True
        except sqlite3.Error:
            return False

    @staticmethod
    @open_con
    def delete_info(table: str, cursor, **kwargs):
        try:
            query = Files.form_delete_query(table, kwargs)
            cursor.execute(query)
            return True
        except sqlite3.Error:
            return False

    @staticmethod
    @open_con
    def return_all(table, cursor):
        cursor.execute(f"SELECT * FROM {table}")
        return cursor.fetchall()
