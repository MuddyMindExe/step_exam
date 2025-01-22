from abc import ABC
from abc import abstractmethod
from sql import SQL


class Object(ABC):  # <- Абстрактный класс
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class Employee(Object):  # <- Класс для добавления/удаления данных о работниках
    def __init__(self, name: str, position: str, phone: int, mail: str):
        self.name = name
        self.position = position
        self.phone = phone
        self.mail = mail

    def add(self):
        return SQL('employees').add_info(name=self.name, position=self.position,
                                         phone=self.phone, mail=self.mail)

    def delete(self):
        return SQL('employees').delete_info(name=self.name, position=self.position,
                                            phone=self.phone, mail=self.mail)

    def get_id(self):
        return SQL('employees').return_info('id', name=self.name, position=self.position,
                                            phone=self.phone, mail=self.mail)


class Book(Object):  # <- Класс для добавления/удаления данных о книгах
    def __init__(self, name: str, year: int, author: str, genre: str, buy_price: int, sell_price: int):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.buy_price = buy_price
        self.sell_price = sell_price

    def add(self):
        return SQL('books').add_info(name=self.name, year=self.year,
                                     author=self.author, genre=self.genre,
                                     buy_price=self.buy_price, sell_price=self.sell_price)

    def delete(self):
        return SQL('books').delete_info(name=self.name, year=self.year,
                                        author=self.author, genre=self.genre,
                                        buy_pice=self.buy_price, sell_price=self.sell_price)

    def get_id(self):
        return SQL('books').return_info('id', name=self.name, year=self.year,
                                        author=self.author, genre=self.genre,
                                        buy_pice=self.buy_price, sell_price=self.sell_price)


class Sell(Object):  # <- Класс для добавления/удаления данных о продажах
    def __init__(self, employee: Employee, book: Book, date: str):
        self.employee = employee
        self.book = book
        self.date = date
        self.profit = self.book.sell_price - self.book.buy_price

    def add(self):
        return SQL('sells').add_info(employee_id=self.employee.get_id(), book_id=self.book.get_id(),
                                     date=self.date, profit=self.profit)

    def delete(self):
        return SQL('sells').delete_info(employee_id=self.employee.get_id(), book_id=self.book.get_id(),
                                        date=self.date, profit=self.profit)
