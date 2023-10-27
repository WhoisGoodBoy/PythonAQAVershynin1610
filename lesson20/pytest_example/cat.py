

class Cat:
    def __init__(self, name, color, age, breed):
        self.__name = name
        self.__color = color
        self.__age = age
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def grow(self):
        self.__age +=1

    @property
    def age(self):
        return self.__age
