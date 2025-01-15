import sqlite3


class SQL:
    @staticmethod
    def init():
        Query.create_table(table_name='employees', name=['TEXT', 'NOT NULL'], position=['TEXT', 'NOT NULL'],
                           phone=['INTEGER', 'NOT NULL'], mail=['TEXT', 'NOT NULL'])

        Query.create_table(table_name='books', name=['TEXT', 'NOT NULL'], year=['INTEGER', 'NOT NULL'],
                           author=['TEXT', 'NOT NULL'], genre=['TEXT', 'NOT NULL'],
                           buy_price=['INTEGER', 'NOT NULL'], sell_price=['INTEGER', 'NOT NULL'])

        Query.create_table(table_name='sells', employee_id=['INTEGER', 'NOT NULL'], book_id=['INTEGER', 'NOT NULL'],
                           date=['TEXT', 'NOT NULL'], profit=['INTEGER', 'NOT NULL'])

    @staticmethod
    def duplicate(table, *args):
        all_data = Query.return_all(table)
        wanted_column = tuple([_ for _ in args])
        return wanted_column in all_data

    @staticmethod
    def add_info(table: str, args):
        return Query.add(table, args)

    @staticmethod
    def delete_info(table: str, cursor, **kwargs):
        try:
            query = Query.form_delete_query(table, kwargs)
            cursor.execute(query)
            return True
        except sqlite3.Error:
            return False


class Query:
    @staticmethod
    def open_con(func):
        def wrap(table, database_name, *args):
            con = sqlite3.connect(f'{database_name}.db')
            cursor = con.cursor()
            SQL.init()
            func(table, cursor, *args)
            con.commit()
            con.close()
        return wrap

    @staticmethod
    def try_except(func):
        def wrap():
            try:
                func()
            except sqlite3.Error:
                return False
        return wrap

    @staticmethod
    def form_add_query(table: str, *args):
        columns = ', '.join(el for el in args)
        placeholders = ', '.join(['?'] * len(args))
        query = f"""INSERT INTO {table} ({columns}) Values ({placeholders})"""
        return query.strip()

    @staticmethod
    def form_delete_query(table: str, columns: dict):
        where = " AND ".join([f'{column} = ?' for column in columns.keys()])
        query = f"""DELETE FROM {table} WHERE {where}"""
        return query.strip()

    @staticmethod
    def form_create_table_query(table_name, **columns):
        sql_columns = ''
        for column_name, column_params in columns.items():
            sql_columns += f"{column_name} {' '.join(column_params)}, "
        query = f'''CREATE TABLE IF NOT EXISTS {table_name} ({sql_columns})'''
        return query.strip()

    @staticmethod
    @open_con
    @try_except
    def create_table(table_name, cursor, **columns):
        query = Query.form_create_table_query(table_name, **columns)
        cursor.execute(query)
        return True

    @staticmethod
    @open_con
    @try_except
    def add(table_name, cursor, *args):
        query = Query.form_add_query(table_name)
        cursor.execute(query, tuple(args))
        return True

    @staticmethod
    @open_con
    @try_except
    def return_all(table_name, cursor):
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()

