from files import Files
import datetime


class Sorted:
    @staticmethod
    def line_to_array(string: str):
        return string.split(', ')

    @staticmethod
    def sells_of_period(start_date, end_date):
        lines = Files.return_strings('sells', 'r')
        return [Sorted.line_to_array(line) for line in lines]


def dt():
    dt1 = datetime.datetime.now()
    print(dt1)
    dt1 += datetime.datetime(0, 0, 0, 2, 0, 0)
    print(dt1)

dt()
