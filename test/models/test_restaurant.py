import unittest

from src.models.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira", False)
        resultado_esperado = f"Esse restaturante chama {restaurant.restaurant_name} e serve culinária {restaurant.cuisine_type}.\n Esse restaturante está servindo {str(restaurant.number_served)} consumidores desde que está aberto."
        assert resultado_esperado == restaurant.describe_restaurant()

    def test_open_restaurant(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira", False)
        resultado_esperado = f"{restaurant.restaurant_name} agora está aberto!"
        assert resultado_esperado == restaurant.open_restaurant()

    def test_open_restaurant_already_open(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira", True)
        resultado_esperado = f"{restaurant.restaurant_name} já está aberto!"
        assert resultado_esperado == restaurant.open_restaurant()

    def test_close_restaurant(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira", True)
        resultado_esperado = f"{restaurant.restaurant_name} agora está fechado!"
        assert resultado_esperado == restaurant.close_restaurant()

    def test_close_restaurant_already_close(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira", False)
        resultado_esperado = f"{restaurant.restaurant_name} já está fechado!"
        assert resultado_esperado == restaurant.close_restaurant()

    def test_set_number_served(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira", False)

    def test_increment_number_served(self):
        assert False
