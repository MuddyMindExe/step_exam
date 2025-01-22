from _datetime import datetime
from execute import Show


class Modify:  # <- Класс для обработки ошибок и неправильных вводов, ошибок и т.д
    @staticmethod  # <- Декоратор для обработки исключений и вызова функции до момента правильного ввода
    def try_except(func):
        def wrap(*args):
            while True:
                try:
                    return func(*args)
                except(IndexError, ValueError):
                    print('Некорректный ввод данных, повторите попытку')
        return wrap

    @staticmethod
    @try_except  # <- Функция, которая запрашивает у пользователя ввод даты согласно шаблону. Возвращает
    def create_date(query='Введите дату в формате: yyyy.mm.dd: '):
        str_date = input(query)
        date = datetime.strptime(str_date, '%Y.%m.%d')
        return date

    @staticmethod
    @try_except  # <- Функция запрашивает ввод ID и возвращает его, если юзер ввел int
    def create_int(query: str):
        id = int(input(query))
        return id

    @staticmethod  # <- Функция форматирует данные, переданные sql в читаемые принты
    def print_sorted_list(unsorted_list):
        if unsorted_list:
            for arr in unsorted_list:
                print(', '.join(str(el) for el in arr))
        else:
            print('Не найдено данных по таким параметрам')


class SortedData:  # <- Класс для сортировки таблиц по различным данным
    def __init__(self, sells: list):
        self.sells = sells

    def date_check(self):  # <- Пользователь вводил 2 даты и возвращается отфильтрованный
        valid_sales = []
        date_1 = Modify.create_date('Введите первую дату (формат yyyy.mm.dd): ')
        date_2 = Modify.create_date('Введите вторую дату (формат yyyy.mm.dd): ')
        date_1, date_2 = max(date_1, date_2), min(date_1, date_2)
        for sell in self.sells:
            date = datetime.strptime(sell[2], '%Y.%m.%d')
            if date_1 <= date <= date_2:
                valid_sales.append(sell)
        return valid_sales

    def best(self, table_name, *params):  # <- Поиск самого частого элемента путем создания словаря
        indexes = {'employees': 0, 'books': 1}
        index = indexes[table_name]
        all_sells = {}
        id = 0
        count = 0
        for sell in self.sells:
            book = sell[index]
            if book not in all_sells.keys():
                all_sells[book] = 0
            else:
                all_sells[book] += 1
        for book_id, amt in all_sells.items():
            if amt > count:
                id = book_id
                count = amt
        return Show(f'{table_name}', f'{", ".join(params)}', id=id)

    def sum_profit(self):
        return sum(sell[3] for sell in self.sells)


class ExecuteCommand:  # <- Класс-интерфейс, нужден просто для комфортного вызова функций, потом может быть дополнен
    def __init__(self, table_name, *data, **params):
        self.table_name = table_name
        self.data = data
        self.params = params
        self.unsorted_list = Show(f'{self.table_name}', *self.data, **self.params).show()

    def show_obj(self):
        Modify.print_sorted_list(self.unsorted_list)

    def obj_in_period(self):
        sorted_list = SortedData(self.unsorted_list).date_check()
        Modify.print_sorted_list(sorted_list)

    def sum_profit(self):
        sorted_list = SortedData(self.unsorted_list).date_check()
        print(SortedData(sorted_list).sum_profit())

    def best(self, table_name, *params):
        sorted_list = SortedData(self.unsorted_list).date_check()
        best = SortedData(sorted_list).best(table_name, *params)
        print(best)

