import datetime
import classes

class UserInteraction:
    warn = 1

    @staticmethod
    def warning():
        i = input(f"Для взаимодействия с интерфейсом нужно вводить соответствующие данные.\n"
                  f"При вводе цифр не нужно использовать дополнительные пробелы, точки и прочие символы\n"
                  f"1 - Ок\n2 - Больше не напоминать в текущей сессии\n")
        return i

    @staticmethod
    def remember_warning_choice():
        warning = UserInteraction.warning()
        if warning == '1' or warning == '2':
            UserInteraction.warn = warning
            UserInteraction.start()
        else:
            print("Некорректный ввод")
            UserInteraction.warning()

    @staticmethod
    def start():
        if UserInteraction.warn == 1:
            UserInteraction.remember_warning_choice()
        print(f"Выберите, что хотите сделать.\n")
        choice = input(f"1 - Добавить данные\n2 - Удалить данные\n3 - Посмотреть данные\n")
        if choice == '1':
            UserInteraction.choice_add()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print('Некорректный выбор, повторите ввод.')

    @staticmethod
    def choice_add():
        print(f"Выберите, какие данные хотите добавить.\n")
        choice = input(f"1 - Добавить работника\n2 - Добавить книгу\n3 - Добавить продажу\n4 - Назад")
        if choice == '1':
            UserInteraction.employee_information()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            UserInteraction.start()
        else:
            print('Некорректный выбор, повторите ввод.')

    @staticmethod
    def employee_information():
        name = input('Введите имя и фамилию работника: ')
        position = input('Укажите должность работника: ')
        try:
            phone = int(input('Введите номер телефона работника без кода страны: '))
        except ValueError:
            phone = int(input('Введите корректный номер телефона работника без кода страны: '))
        mail = input('Укажите почту работника: ')
        classes.Employee(name, position, phone, mail).add()

    @staticmethod
    def book_information():
        name = input('Введите название книги: ')
        author = input('Введите имя автора книги: ')
        genre = input('Введите жанр книги: ')
        try:
            buy_price = int(input('Введите цену закупки книги: '))
            sell_price = int(input('Введите цену продажи книги: '))
        except ValueError:
            print('Укажите корректные данные')
            buy_price = int(input('Введите цену закупки книги: '))
            sell_price = int(input('Введите цену продажи книги: '))
        classes.