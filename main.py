from sorted import ExecuteCommand, Modify
from execute import Add, Delete, EmployeeBuilder


class Handler:
    handlers = {
        'main_menu': {},
        'add_menu': {},
        'delete_menu': {},
        'view_menu': {},
        'employee_info_menu': {},
        'book_info_menu': {},
        'sells_info_menu': {}
    }

    @staticmethod
    def register_handler(index, description, menu, callback):
        if menu not in Handler.handlers:
            Handler.handlers[menu] = {}
        Handler.handlers[menu][index] = {'desc': description, 'callback': callback}


class UserInteraction:
    warn = 1

    @staticmethod
    def warning():
        warning = input(f"Для взаимодействия с интерфейсом нужно вводить соответствующие данные.\n"
                        f"При вводе цифр не нужно использовать дополнительные пробелы, точки и прочие символы\n"
                        f"1 - Ок\n2 - Больше не напоминать в текущей сессии\n")
        return warning

    @staticmethod
    def remember_warning_choice():
        warning = UserInteraction.warning()
        if warning in ['1', '2']:
            UserInteraction.warn = int(warning)
        else:
            print("Некорректный ввод")
            UserInteraction.warning()

    @staticmethod
    def start_menu(menu_name):
        if UserInteraction.warn == 1:
            UserInteraction.remember_warning_choice()

        menu = Handler.handlers.get(menu_name, {})
        if not menu:
            print(f"Меню '{menu_name}' не существует.")
            return

        while True:
            print(f"Выберите действие:")
            for index, item in menu.items():
                print(f"{index} - {item['desc']}")
            choice = input()

            if choice in menu:
                menu[choice]['callback']()
                UserInteraction.start_menu('main_menu')
            else:
                print('Некорректный выбор, повторите ввод.')

    @staticmethod
    def exit():
        print("Выход из программы.")
        exit(0)


Handler.register_handler('1', 'Добавить данные', 'main_menu',
                         lambda: UserInteraction.start_menu('add_menu'))
Handler.register_handler('2', 'Удалить данные', 'main_menu',
                         lambda: UserInteraction.start_menu('delete_menu'))
Handler.register_handler('3', 'Посмотреть данные', 'main_menu',
                         lambda: UserInteraction.start_menu('view_menu'))
Handler.register_handler('4', 'Выход', 'main_menu',
                         lambda: UserInteraction.exit())

Handler.register_handler('1', 'Добавить работника', 'add_menu',
                         lambda: Add().employee())
Handler.register_handler('2', 'Добавить книгу', 'add_menu',
                         lambda: Add().book())
Handler.register_handler('3', 'Добавить продажу', 'add_menu',
                         lambda: Add().sell())
Handler.register_handler('4', 'Назад', 'add_menu',
                         lambda: UserInteraction.start_menu('main_menu'))

Handler.register_handler('1', 'Удалить работника', 'delete_menu',
                         lambda: Delete().employee())
Handler.register_handler('2', 'Удалить книгу', 'delete_menu',
                         lambda: Delete().book())
Handler.register_handler('3', 'Удалить продажу', 'delete_menu',
                         lambda: Delete().sell())
Handler.register_handler('4', 'Назад', 'delete_menu',
                         lambda: UserInteraction.start_menu('main_menu'))

Handler.register_handler('1', 'Данные о работниках', 'view_menu',
                         lambda: UserInteraction.start_menu('employee_info_menu'))
Handler.register_handler('2', 'Данные о книгах', 'view_menu',
                         lambda: UserInteraction.start_menu('book_info_menu'))
Handler.register_handler('3', 'Данные о продажах', 'view_menu',
                         lambda: UserInteraction.start_menu('sells_info_menu'))
Handler.register_handler('4', 'Назад', 'view_menu',
                         lambda: UserInteraction.start_menu('main_menu'))


Handler.register_handler('1', 'Данные работника о всех работниках', 'employee_info_menu',
                         lambda: ExecuteCommand('employees').show_obj())
Handler.register_handler('2', 'Данные работника по ID', 'employee_info_menu',
                         lambda: ExecuteCommand('employees', id=Modify.create_int('Введите ID: ')).show_obj())
Handler.register_handler('3', 'Данные работника по номеру телефона', 'employee_info_menu',
                         lambda: ExecuteCommand('employees', phone=Modify.create_int('Введите номер: ')).show_obj())
Handler.register_handler('4', 'Назад', 'employee_info_menu',
                         lambda: UserInteraction.start_menu('view_menu'))

Handler.register_handler('1', 'Данные о всех книгах', 'book_info_menu',
                         lambda: ExecuteCommand('books').show_obj())
Handler.register_handler('2', 'Данные о книге по ID', 'book_info_menu',
                         lambda: ExecuteCommand('books', id=Modify.create_int('Введите ID: ')).show_obj())
Handler.register_handler('3', 'Назад', 'book_info_menu',
                         lambda: UserInteraction.start_menu('view_menu'))

Handler.register_handler('1', 'Данные о всех продажах', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').show_obj())
Handler.register_handler('2', 'Данные о всех продажах за конкретную дату', 'sells_info_menu',
                         lambda: ExecuteCommand('sells', date=Modify.create_date()).show_obj())
Handler.register_handler('3', 'Все продажи за определенный промежуток времени', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').obj_in_period())
Handler.register_handler('4', 'Все продажи конкретного сотрудника', 'sells_info_menu',
                         lambda: ExecuteCommand('sells', employee_id=EmployeeBuilder.build().get_id()).show_obj())
Handler.register_handler('5', 'Самая продаваемая книга за определенный промежуток времени', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').best('books', 'name'))
Handler.register_handler('6', 'Самый продуктивный торговца за определенный промежуток времени', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').best('employees', 'name'))
Handler.register_handler('7', 'Суммарная прибыль за определенный промежуток времени', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').sum_profit())
Handler.register_handler('8', 'Самый продаваемый автор за определенный промежуток времени', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').best('books', 'author'))
Handler.register_handler('9', 'Самый продаваемый жанр за определенный промежуток времени', 'sells_info_menu',
                         lambda: ExecuteCommand('sells').best('books', 'genre'))

if __name__ == "__main__":
    UserInteraction.start_menu('main_menu')
