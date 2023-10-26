from lesson19.proxy.reader import Reader

class CsvProxyReader(Reader):
    def __init__(self, csv_reader):
        self.__result = ""
        self.__is_actual = False
        self.__reader = csv_reader

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read()
            self.update_actual_result(True)
            return self.__result


    def update_actual_result(self, status):
        self.__is_actual = status