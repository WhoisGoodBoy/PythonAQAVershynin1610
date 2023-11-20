import pytest
from lesson27.infrastucture.planet_service import PlanetService
import json


@pytest.fixture()
def planet_service():
    return PlanetService()


@pytest.fixture()
def planet_1():
    with open('tatooine.json', 'r') as tatooine:
        return json.load(tatooine)
