from abc import ABC
from abc import abstractmethod
from sql import SQL


class Object(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def show_current(self):
        pass

    @abstractmethod
    def show_all(self):
        pass


class Employee(Object):
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

    def show_current(self):
        return f"Name: {self.name}\nPosition: {self.position}\nPhone Number: {self.phone}\nEmail address: {self.mail}"

    def get_id(self):
        return SQL('employees').return_info('id', name=self.name, position=self.position,
                                            phone=self.phone, mail=self.mail)

    def show_all(self):
        pass
        # records = SQL().return_all('employees')
        # for record in records:
        #     print(f"Name: {record[0]}, Position: {record[1]}, Phone: {record[2]}, Mail: {record[3]}\n")


class Book(Object):
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

    def show_current(self):
        return f"Name: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}\n" \
               f"Original price: {self.buy_price}\nSelling price: {self.sell_price}"

    def get_id(self):
        return SQL('books').return_info('id', name=self.name, year=self.year,
                                        author=self.author, genre=self.genre,
                                        buy_pice=self.buy_price, sell_price=self.sell_price)

    def show_all(self):
        pass
        # records = SQL().return_all('books')
        # for record in records:
        #     print(f"ID: {record[0]}Name: {record[1]}, Year: {record[2]}, Author: {record[3]}, Genre: {record[4]}"
        #           f"Buy price: {record[5]}, Sell price: {record[6]}\n")


class Sell(Object):
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

    def show_current(self):
        return f"Employee: {self.employee}\nBook: {self.book.name}\nDate: {self.date}\nProfit: {self.profit}"

    def show_all(self):
        pass
