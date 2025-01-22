from abc import ABC
from abc import abstractmethod
from classes import Employee, Book, Sell, SQL


class Execute(ABC):  # <- Абстрактный класс для Add и Delete
    @abstractmethod
    def employee(self):
        pass

    @abstractmethod
    def book(self):
        pass

    @abstractmethod
    def sell(self):
        pass


class Add(Execute):  # <- Создает объекты класса и обращается к нужным методам
    def employee(self):
        employee = EmployeeBuilder.build()
        employee.add()

    def book(self):
        book = BookBuilder.build()
        book.add()

    def sell(self):
        sell = SellBuilder.build()
        sell.add()


class Delete(Execute):  # <- Создает объекты класса и обращается к нужным методам
    def employee(self):
        employee = EmployeeBuilder.build()
        employee.delete()

    def book(self):
        book = BookBuilder.build()
        book.delete()

    def sell(self):
        sell = SellBuilder.build()
        sell.delete()


class Show:  # <- Функция возвращает сырой список из кортежей, полученных из таблицы SQL
    def __init__(self, table_name, *args, **kwargs):
        self.table_name = table_name
        self.args = args
        self.kwargs = kwargs

    def show(self):
        return SQL(f"{self.table_name}").return_info(*self.args, **self.kwargs)


class EmployeeBuilder:  # <- Класс строитель объекта класса по введенным данным
    @staticmethod
    def build():
        name = input('Введите имя и фамилию работника: ')
        position = input('Укажите должность работника: ')
        try:
            phone = int(input('Введите номер телефона работника без кода страны: '))
        except ValueError:
            phone = int(input('Введите корректный номер телефона работника без кода страны: '))
        mail = input('Укажите почту работника: ')
        return Employee(name, position, phone, mail)


class BookBuilder:  # <- Класс строитель объекта класса по введенным данным
    @staticmethod
    def build():
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
        return Book(name, year, author, genre, buy_price, sell_price)


class SellBuilder:  # <- Класс строитель объекта класса по введенным данным
    @staticmethod
    def build():
        employee = EmployeeBuilder.build()
        book = BookBuilder.build()
        date = input('Введите дату продажи в формате: yyyy.mm.dd: ')
        return Sell(employee, book, date)



