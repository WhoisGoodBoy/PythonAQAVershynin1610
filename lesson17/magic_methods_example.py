import datetime

class SmallMotorcycle:
    list_of_calls_to_unexisting_parameters = []
    def __init__(self):
        self.color = 'white'

    def __str__(self):
        return f'I`m a small bycicle colored in {self.color}'

    def __repr__(self):
        return 'SmallMotorcycle()'

    def __getattr__(self, item):
        self.list_of_calls_to_unexisting_parameters.append((item, datetime.datetime.now()))
        return f'there`s no such method as {item}'


small_moto = SmallMotorcycle()
print(small_moto.engine)
print(small_moto)



'''second_cmall_moto = eval(repr(small_moto))
print(id(small_moto))
print(second_cmall_moto)'''

c = eval('1.1 + 2')
print(type(c))
