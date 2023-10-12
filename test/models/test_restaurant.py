import unittest

from src.models.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        resultado_esperado = f"Esse restaturante chama {restaurant.restaurant_name} e serve culinária {restaurant.cuisine_type}.\n Esse restaturante está servindo {str(restaurant.number_served)} consumidores desde que está aberto."
        assert resultado_esperado == restaurant.describe_restaurant()

    def test_open_restaurant(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        resultado_esperado = f"{restaurant.restaurant_name} agora está aberto!"
        assert resultado_esperado == restaurant.open_restaurant()
        assert restaurant.open.__eq__(True)
        assert restaurant.number_served == 0

    def test_open_restaurant_already_open(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()
        resultado_esperado = f"{restaurant.restaurant_name} já está aberto!"
        assert resultado_esperado == restaurant.open_restaurant()

    def test_close_restaurant(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()
        resultado_esperado = f"{restaurant.restaurant_name} agora está fechado!"
        assert resultado_esperado == restaurant.close_restaurant()
        assert restaurant.open.__eq__(False)

    def test_close_restaurant_already_close(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.close_restaurant()
        resultado_esperado = f"{restaurant.restaurant_name} já está fechado!"
        assert resultado_esperado == restaurant.close_restaurant()

    def test_set_number_served_by_restaurant_closed(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        resultado_esperado = f"{restaurant.restaurant_name} está fechado!"
        resultado = (restaurant.set_number_served(20))
        assert resultado == resultado_esperado

    def test_set_number_served_negative(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()
        resultado = restaurant.set_number_served(-1)
        resultado_esperado = "A quantidade de pessoas não pode ser menor que zero"
        assert resultado_esperado == resultado

    def test_set_number_served(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()
        resultado_esperado = restaurant.set_number_served(10)
        assert resultado_esperado.__eq__(10)

    def test_set_number_served_cannot_is_string(self):
        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()
        resultado = restaurant.set_number_served("assd")
        resultado_esperado = "Digite apenas números"
        assert resultado_esperado == resultado

    def test_increment_number_served(self):
        QUANTIDADE_INICIAL = 10
        QUANTIDADE_ACRESCIDO = 10

        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()

        resultado_esperado = QUANTIDADE_INICIAL + QUANTIDADE_ACRESCIDO
        restaurant.set_number_served(QUANTIDADE_INICIAL)
        resultado = restaurant.increment_number_served(QUANTIDADE_ACRESCIDO)

        assert restaurant.open
        assert resultado == resultado_esperado

    def test_increment_number_served_negative_number(self):
        QUANTIDADE_ACRESCIDO = -10

        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()

        resultado = "A quantidade de pessoas não pode ser menor que zero"
        resultado_esperado = restaurant.increment_number_served(QUANTIDADE_ACRESCIDO)

        assert resultado_esperado == resultado

    def test_increment_number_cannot_is_string(self):
        QUANTIDADE_ACRESCIDO = "10"

        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.open_restaurant()

        resultado = "Digite apenas números"
        resultado_esperado = restaurant.increment_number_served(QUANTIDADE_ACRESCIDO)
        assert resultado_esperado == resultado

    def test_increment_number_with_restaurant_closed(self):
        QUANTIDADE_ACRESCIDO = 10

        restaurant = Restaurant("Restaurante teste", "Brasileira")
        restaurant.close_restaurant()

        resultado = f"{restaurant.restaurant_name} está fechado!"
        resultado_esperado = restaurant.increment_number_served(QUANTIDADE_ACRESCIDO)
        assert resultado_esperado == resultado
