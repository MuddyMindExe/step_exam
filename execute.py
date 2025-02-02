from abc import ABC
from abc import abstractmethod
from classes import Employee, Book, Sell
from db import DatabaseInterface


class Execute(ABC):  # <- Абстрактный класс для Add и Delete
    @abstractmethod
    def execute(self, obj):
        pass


class Add(Execute):  # <- Создает объекты класса и обращается к нужным методам
    def execute(self, obj):
        obj.add()


class Delete(Execute):  # <- Создает объекты класса и обращается к нужным методам
    def execute(self, obj):
        obj.delete()


class Show:  # <- Функция возвращает сырой список из кортежей, полученных из таблицы SQL
    def __init__(self, db: DatabaseInterface, *args, **kwargs):
        self.db = db
        self.args = args
        self.kwargs = kwargs

    def show(self):
        data = self.db.return_info(*self.args, **self.kwargs)
        return data if data else "Нет данных."


class EmployeeBuilder:  # <- Класс строитель объекта класса по введенным данным
    @staticmethod
    def build(db: DatabaseInterface):
        name = input('Введите имя и фамилию работника: ')
        position = input('Укажите должность работника: ')
        try:
            phone = int(input('Введите номер телефона работника без кода страны: '))
        except ValueError:
            phone = int(input('Введите корректный номер телефона работника без кода страны: '))
        mail = input('Укажите почту работника: ')
        return Employee(db, name, position, phone, mail)


class BookBuilder:  # <- Класс строитель объекта класса по введенным данным
    @staticmethod
    def build(db: DatabaseInterface):
        name = input('Введите название книги: ')
        year = int(input('Укажите год выпуска книги: '))
        author = input('Введите имя автора книги: ')
        genre = input('Введите жанр книги: ')
        try:
            buy_price = int(input('Введите цену закупки книги: '))
            sell_price = int(input('Введите цену продажи книги: '))
        except ValueError:
            print('Укажите корректные данные')
            buy_price = int(input('Введите цену закупки книги: '))
            sell_price = int(input('Введите цену продажи книги: '))
        return Book(db, name, year, author, genre, buy_price, sell_price)


class SellBuilder:  # <- Класс строитель объекта класса по введенным данным
    @staticmethod
    def build(db: DatabaseInterface):
        employee = EmployeeBuilder.build(db)
        book = BookBuilder.build(db)
        date = input('Введите дату продажи в формате: yyyy.mm.dd: ')
        return Sell(db, employee, book, date)
