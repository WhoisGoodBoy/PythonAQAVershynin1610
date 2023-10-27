from lesson20.abstract_factory_example.beer_factory import BeerFactory
from lesson20.abstract_factory_example.christmas import Christmas



class StoutFactory(BeerFactory):
    _beer_type = 'Stout'

    def __init__(self):
        self.__name = 'First Private Brewery'
        self.__positions = ['Christmas', 'Dark', 'Special']

    @property
    def positions(self):
        return  self.__positions

    def get_beer(self, name):
        if name == 'Christmas':
            return Christmas()
        elif name == 'Dark':
            return 'your Dark nectar sir'
        elif name == 'Special':
            return 'your Special nectar sir'
        else:
            return'sorry dude'
