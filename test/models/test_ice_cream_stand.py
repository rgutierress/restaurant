import pytest
import sys
from io import StringIO


from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand():

    # Teste com uma lista não vazia
    def test_flavors_available_non_empty(self):
        ##Setup
        list_flavors_available = ["Morango", "Chocolate", "Baunilha", "Pistache"]
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_available)

        ##Chamada
        result = iceCream.flavors_available()

        ##Avaliação
        assert result == list_flavors_available

    # Teste com uma lista vazia
    def test_flavors_available_empty(self):
        ##Setup
        list_flavors_empty = []
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_empty)

        ##Chamada
        result = iceCream.flavors_available()

        ##Avaliação
        assert result == []

    # Teste com saída impressa
    @pytest.mark.usefixtures('capsys')
    def test_flavors_available_output(capsys):
        ##Setup
        list_flavors_available = ["Morango", "Chocolate", "Baunilha", "Pistache"]
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_available)

        # Redirecione a saída padrão para um buffer
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Chame o método flavors_available
        iceCream.flavors_available()

        # Recupere a saída capturada
        output = sys.stdout.getvalue()

        # Restaure a saída padrão original
        sys.stdout = original_stdout

        ##Avaliação
        assert "No momento temos os seguintes sabores de sorvete disponíveis:" in output
        assert "Estamos sem estoque atualmente!" not in output

    # Teste com lista de sabores None
    def test_flavors_available_none(self):
        ##Setup
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", None)

        ##Chamada
        result = iceCream.flavors_available()

        ##Avaliação
        assert result == []

    # Teste para sabor disponível
    def test_find_flavor_available(self):
        ##Setup
        list_flavors_available = ["Morango", "Chocolate", "Baunilha", "Pistache"]
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_available)

        ##Chamada
        result = iceCream.find_flavor("Morango")

        ##Avaliação
        assert result == "O sabor 'Morango' está disponível no momento."

    # Teste para sabor não disponível
    def test_find_flavor_not_available(self):
        ##Setup
        list_flavors_available = ["Morango", "Chocolate", "Baunilha", "Pistache"]
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_available)

        ##Chamada
        result = iceCream.find_flavor("Caramelo")

        ##Avaliação
        assert result == "O sabor 'Caramelo' não está disponível no momento."

    def test_find_flavor_empty_list(self):
        ##Setup
        list_flavors_empty = []
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_empty)

        ##Chamada
        result = iceCream.find_flavor('Pistache')

        ##Avaliação
        assert result == "Estamos sem estoque atualmente."

    # Teste para adicionar sabor que já está disponível
    def test_add_flavor_already_available(self):
        ##Setup
        list_flavors_available = ["Morango", "Chocolate", "Baunilha", "Pistache"]
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_available)

        ##Chamada
        result = iceCream.add_flavor("Baunilha")

        ##Avaliação
        assert result == "O sabor 'Baunilha' já está disponível no estoque."

    # Teste para adicionar sabor quando a sorveteria está fechada
    def test_add_flavor_when_closed(self):
        ##Setup
        list_flavors_available = ["Morango", "Chocolate", "Baunilha", "Pistache"]

        ##Chamada
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_available, open=False)
        result = iceCream.add_flavor("Caramelo")

        ##Avaliação
        assert result == "A sorveteria está fechada, não é possível adicionar sabores."

    # Teste para adicionar sabor quando a lista de sabores está vazia
    def test_add_flavor_to_empty_list(self):
        ##Setup
        list_flavors_empty = []
        iceCream = IceCreamStand("Minha Sorveteria", "Sorvetes", list_flavors_empty)

        result = iceCream.add_flavor("Caramelo")
        assert result == "O sabor 'Caramelo' foi adicionado ao estoque."
