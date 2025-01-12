from abc import ABC
from abc import abstractmethod
from sql import Files


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
        self.args = [self.name, self.position, self.phone, self.mail]

    # def add(self):
    #     if not Files.duplicate(self.args):
    #         Files.add_info('employee', 'a+', *self.args)
    #         return True
    #     else:
    #         return False
    # принт перенести в класс интерфейса

    def add(self):
        if not Files.duplicate(self.args):
            Files.add_info('employee', 'a+', *self.args)
        else:
            print("This employee is already in database")

    def delete(self):
        Files.delete_info('employee', 'w', *self.args)

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
        self.args = [self.name, self.year, self.author, self.genre, self.buy_price, self.sell_price]

    def add(self):
        if not Files.duplicate(self.args):
            Files.add_info('book', 'a+', *self.args)
        else:
            print("This employee is already in database")

    def delete(self):
        Files.delete_info('book', 'w', *self.args)

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
        Files.add_info('sell', 'a+', self.employee, self.book, self.date, self.profit)

    def delete(self):
        Files.delete_info('sell', 'w', self.employee, self.book, self.date, self.profit)

    def show(self):
        return f"Employee: {self.employee}\nBook: {self.book.name}\nDate: {self.date}\nProfit: {self.profit}"
