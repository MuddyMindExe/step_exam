from abc import ABC
from abc import abstractmethod
from files import Files


class Object(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Employee(Object):
    def __init__(self, name: str, position: str, phone: int, mail: str):
        self.name = name
        self.position = position
        self.phone = phone
        self.mail = mail

    def add(self):
        pass

    def delete(self):
        pass

    def show(self):
        return f"Name: {self.name}\nPosition: {self.position}\nPhone Number: {self.phone}\nEmail address: {self.mail}"


class Book(Object):
    def __init__(self, name: str, year: int, author: str, genre: str, buy_price: int, sell_price: int):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.buy_price = buy_price
        self.sell_price = sell_price

    def add(self):
        pass

    def delete(self):
        pass

    def show(self):
        return f"Name: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}\n" \
               f"Original price: {self.buy_price}\nSelling price: {self.sell_price}"


class Sell(Object):
    def __init__(self, employee: Employee, book: Book, date: str):
        self.employee = employee
        self.book = book
        self.date = date
        self.profit = self.book.sell_price - self.book.buy_price

    def add(self):
        pass

    def delete(self):
        pass

    def show(self):
        return f"Employee: {self.employee}\nBook: {self.book.name}\nDate: {self.date}\nProfit: {self.profit}"
