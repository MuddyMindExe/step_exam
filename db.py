from abc import ABC, abstractmethod
from sql import SQL


class DatabaseInterface(ABC):
    @abstractmethod
    def add_info(self, **kwargs):
        pass

    @abstractmethod
    def delete_info(self, **kwargs):
        pass

    @abstractmethod
    def return_info(self, *args, **kwargs):
        pass


class SQLite(DatabaseInterface):
    def __init__(self, table_name):
        self.SQL = SQL(table_name)

    def add_info(self, **kwargs):  # <- Функция добавления данных
        return self.SQL.add_info(**kwargs)

    def delete_info(self, **kwargs):  # <- Функция удаления данных
        return self.SQL.delete_info(**kwargs)

    def return_info(self, *args, **kwargs):  # <- Функция читки данных из таблиц
        return self.SQL.return_info(*args, **kwargs)
