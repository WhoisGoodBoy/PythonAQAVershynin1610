from lesson20.abstract_factory_example.stout_factory import StoutFactory
from lesson20.abstract_factory_example.lager_factory import LagerFactory



class BeerFactoryFactory:

    def get_beer_factory(self,name):
        if name == 'Stout':
            return StoutFactory()
        else:
            return LagerFactory()


bff = BeerFactoryFactory()
stout_f = bff.get_beer_factory('Stout')
cristmas_stout = stout_f.get_beer('Christmas')
sip = cristmas_stout.make_a_sip()
print(sip)