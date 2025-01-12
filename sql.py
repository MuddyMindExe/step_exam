import sqlite3


class Files:
    @staticmethod
    def open_con(func):
        def wrap():
            con = sqlite3.connect('bookstore.db')
            cursor = con.cursor()
            func(cursor)
            con.commit()
            con.close()

        return wrap

    @open_con
    def __init__(self, cursor):
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
            employee_phone INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            date DATETIME NOT NULL,
            profit INTEGER NOT NULL
        )
        ''')

    @staticmethod
    def duplicate(file, args):
        line = Files.form_string(args)

    def form_query(self):
        pass

    @staticmethod
    def form_string(args):
        return ', '.join(str(val) for val in args) + '\n'

    @staticmethod
    def return_strings(file):
        return file.readlines()

    @staticmethod
    def add_info(file, *args):
        string = Files.form_string(args)
        file.write(string)

    @staticmethod
    def delete_info(file, *args):
        line_to_remove = Files.form_string(args)
        lines = file.readlines()
        lines.remove(line_to_remove)
        for line in lines:
            file.write(line)

    # Функцию ниже переделать.
    # Должна возвращать массив всего находящегося в файле. Отдельная функция массив обрабатывает
    @staticmethod
    def show_info(file):
        lines = file.readlines()
        for line in lines:
            for el in line.split(', '):
                print(el + '\n')
        return [line for line in lines]
