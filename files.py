class Files:
    @staticmethod
    def open():
        def wrap(*args):
            files = {'employee': 'employees.txt', 'book': 'books.txt', 'sell': 'sells.txt'}
        return wrap

    def add_info(self):
        pass

    def delete_info(self):
        pass

    def show_info(self, file):
        return file
