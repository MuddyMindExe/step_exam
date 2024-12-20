class Files:
    @staticmethod
    def open(func):
        def wrap(file_to_open, mode, **kwargs):
            files = {'employee': 'employees.txt', 'book': 'books.txt', 'sell': 'sells.txt'}
            file_to_open = files[file_to_open]
            with open(file_to_open, mode) as file:
                func(file, **kwargs)
        return wrap

    @staticmethod
    def form_string(args):
        return ', '.join(str(val) for val in args) + '\n'

    @staticmethod
    @open
    def add_info(file, *args):
        string = Files.form_string(args)
        file.write(string)

    @staticmethod
    @open
    def delete_info(file, *args):
        line_to_remove = Files.form_string(args)
        lines = file.readlines()
        lines.remove(line_to_remove)
        for line in lines:
            file.write(line)

    @staticmethod
    @open
    def show_info(file):
        lines = file.readlines()
        for line in lines:
            for el in line.split(', '):
                print(el + '\n')
