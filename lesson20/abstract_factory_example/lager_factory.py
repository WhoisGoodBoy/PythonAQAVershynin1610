from lesson20.abstract_factory_example.beer_factory import BeerFactory


class LagerFactory(BeerFactory):
    _beer_type = 'Lager'

    def __init__(self):
        self.__name= 'Opillya'
        self.__positions = ['Light', 'Honeybeer', 'Wheat']

    @property
    def positions(self):
        return self.__positions

    def get_beer(self, name):
        if name == 'Light':
            return 'light beer sir'
        elif name == 'Honeybeer':
            return 'Honeybeer sir'
        elif name == 'Wheat':
            return 'Wheat sir'
        else:
            return'sorry dude'


factory = LagerFactory()
light = factory.get_beer('Light')