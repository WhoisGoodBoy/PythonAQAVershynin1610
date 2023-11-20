def test_planet_1(planet_service):
    tatooine_response = planet_service.get_planet(1)
    assert tatooine_response.json()["name"] == "Tatooine"
    assert tatooine_response.status_code == 200

def test_planet_1_with_multiple_fixtures(planet_service,planet_1):
    tatooine_response = planet_service.get_planet(1)
    assert tatooine_response.json() == planet_1

def test_planets_pagination(planet_service):
    list_of_planets = planet_service.get_planets(2)
    assert list_of_planets.json()["next"] == "https://swapi.dev/api/planets/?page=3"