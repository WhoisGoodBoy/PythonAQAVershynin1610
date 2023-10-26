from lesson19.proxy.reader import Reader

class CsvReader(Reader):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename) as file:
            text = file.read()
        return text
