from requests import get
from lesson27.app import config


class PlanetService:
    def __init__(self):
        self.planet_url = f'{config["host"]}/planets/'

    def get_planet(self, planet_id):
        return get(f'{self.planet_url}{planet_id}/')

    def get_planets(self, pagination_page=1):
        return get(f'{self.planet_url}?page={pagination_page}')