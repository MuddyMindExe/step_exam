import sqlite3


class SQL:  # <- Класс-интерфейс, просто вызывает функции и возвращает результат их выполнения
    def __init__(self, table_name):
        self.table_name = table_name
        ExecuteQuery("employees").create_table(id=['INTEGER', 'PRIMARY KEY', 'AUTOINCREMENT'],
                                               name=['TEXT', 'NOT NULL'], position=['TEXT', 'NOT NULL'],
                                               phone=['INTEGER', 'NOT NULL'], mail=['TEXT', 'NOT NULL'])

        ExecuteQuery("books").create_table(id=['INTEGER', 'PRIMARY KEY', 'AUTOINCREMENT'],
                                           name=['TEXT', 'NOT NULL'], year=['INTEGER', 'NOT NULL'],
                                           author=['TEXT', 'NOT NULL'], genre=['TEXT', 'NOT NULL'],
                                           buy_price=['INTEGER', 'NOT NULL'], sell_price=['INTEGER', 'NOT NULL'])

        ExecuteQuery("sells").create_table(employee_id=['INTEGER', 'NOT NULL'],
                                           book_id=['INTEGER', 'NOT NULL'],
                                           date=['TEXT', 'NOT NULL'], profit=['INTEGER', 'NOT NULL'])

    def add_info(self, **kwargs):  # <- Функция добавления данных
        return ExecuteQuery(self.table_name).add(**kwargs)

    def delete_info(self, **kwargs):  # <- Функция удаления данных
        return ExecuteQuery(self.table_name).delete(**kwargs)

    def return_info(self, *args, **kwargs):  # <- Функция читки данных из таблиц
        return ExecuteQuery(self.table_name).return_info(*args, **kwargs)


class ExecuteQuery:
    def __init__(self, table_name):
        self.table_name = table_name
        self.con = sqlite3.connect(f'bookstore.db', isolation_level=None)
        self.cursor = self.con.cursor()

    def create_table(self, **columns):
        query = FormQuery(self.table_name).form_create_table_query(**columns)
        self.cursor.execute(query)
        return True

    def add(self, **kwargs):
        query = FormQuery(self.table_name).form_add_query(**kwargs)
        self.cursor.execute(query, tuple(kwargs.values()))
        return True

    def delete(self, **kwargs):
        query = FormQuery(self.table_name).form_delete_query(**kwargs)
        self.cursor.execute(query, tuple(kwargs.values()))
        return True

    def return_info(self, *args, **kwargs):
        query = FormQuery(self.table_name).form_find_query(*args, **kwargs)
        self.cursor.execute(query)
        return self.cursor.fetchall()


class FormQuery:
    def __init__(self, table_name):
        self.table_name = table_name

    def form_create_table_query(self, **columns):
        sql_columns = ', '.join(
            f"{column_name} {' '.join(column_params)}" for column_name, column_params in columns.items()
        )
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} ({sql_columns})'''
        return query.strip()

    def form_add_query(self, **kwargs):
        columns = ', '.join(str(el) for el in kwargs.keys())
        placeholders = ', '.join(['?'] * len(kwargs))
        query = f"""INSERT INTO {self.table_name} ({columns}) Values ({placeholders})"""
        return query.strip()

    def form_delete_query(self, **columns):
        where = " AND ".join([f'{column} = ?' for column in columns.keys()])
        query = f"""DELETE FROM {self.table_name} WHERE {where}"""
        return query.strip()

    def form_find_query(self, *required_columns, **filters):
        required = ', '.join(required_columns) if required_columns else '*'
        if filters:
            conditions = " AND ".join(f"{column}='{value}'"
                                      if isinstance(value, str) else f"{column}={value}"
                                      for column, value in filters.items())
            additional_parameters = f" WHERE {conditions}"
        else:
            additional_parameters = ""
        query = f"SELECT {required} FROM {self.table_name}" + additional_parameters
        return query.strip()
