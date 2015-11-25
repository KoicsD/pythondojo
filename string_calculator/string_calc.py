__author__ = 'KoicsD'

class StringCalc:
    @staticmethod
    def add(num_as_str: str):
        if num_as_str == "":
            return 0
        delimiter = ','
        if num_as_str[0] == '\\':
            delimiter = num_as_str[1]
            num_as_str = num_as_str[2:]
        splitted = num_as_str.split(delimiter)
        parsed = [int(i) for i in splitted]
        return sum(parsed)