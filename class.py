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
        return Files.add_info('employees', *[self.name, self.position, self.phone, self.mail])

    def delete(self):
        return Files.delete_info('employees', name=self.name, position=self.position, phone=self.phone, mail=self.mail)

    def show_current(self):
        return f"Name: {self.name}\nPosition: {self.position}\nPhone Number: {self.phone}\nEmail address: {self.mail}"

    def show_all(self):
        records = Files.return_all('employees')
        for record in records:
            print(f"Name: {record[0]}, Position: {record[1]}, Phone: {record[2]}, Mail: {record[3]}\n")


class Book(Object):
    def __init__(self, name: str, year: int, author: str, genre: str, buy_price: int, sell_price: int):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.buy_price = buy_price
        self.sell_price = sell_price

    def add(self):
        return Files.add_info('books', *[self.name, self.year, self.author, self.genre, self.buy_price, self.sell_price])

    def delete(self):
        return Files.delete_info('books', name=self.name, year=self.year,
                                 author=self.author, genre=self.genre,
                                 buy_pice=self.buy_price, sell_price=self.sell_price)

    def show_current(self):
        return f"Name: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}\n" \
               f"Original price: {self.buy_price}\nSelling price: {self.sell_price}"

    def show_all(self):
        records = Files.return_all('books')
        for record in records:
            print(f"ID: {record[0]}Name: {record[1]}, Year: {record[2]}, Author: {record[3]}, Genre: {record[4]}"
                  f"Buy price: {record[5]}, Sell price: {record[6]}\n")


class Sell(Object):
    def __init__(self, employee: Employee, book: Book, date: str):
        self.employee = employee
        self.book = book
        self.book_id = str(book.year)+book.name[:3]+book.author[:3]
        self.date = date
        self.profit = self.book.sell_price - self.book.buy_price

    def add(self):
        return Files.add_info('sells', *[self.employee.phone, self.book_id, self.date, self.profit])

    def delete(self):
        return Files.delete_info('employee_id', employee_id=self.employee.phone, book_id=self.book_id,
                                 date=self.date, profit=self.profit)

    def show_current(self):
        return f"Employee: {self.employee}\nBook: {self.book.name}\nDate: {self.date}\nProfit: {self.profit}"

    def show_all(self):
        records = Files.return_all('sells')
        for record in records:
            print(f"Employee: {record[0]}, Book: {record[1]}, Date: {record[2]}, Profit: {record[3]}\n")
