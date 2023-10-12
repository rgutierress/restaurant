from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list, open=True):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.open = open
        self.flavors = flavors_list

    # Refactory:
    # 1. Uma lista vazia chamada available_flavors foi criada para armazenar os sabores disponíveis. Isso permite que a função acumule os sabores disponíveis na lista.
    # 2. Em vez de usar print para mostrar os sabores na saída, a função agora usa append para adicionar cada sabor à lista available_flavors.
    # 3. A função retorna a lista available_flavors quando termina de percorrer os sabores.
    # 4. Se a lista de sabores estiver vazia, a função retorna uma lista vazia, indicando que não há sabores disponíveis.
    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            available_flavors = []
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                available_flavors.append(flavor)
                print(f"\t-{flavor}")
            return available_flavors
        else:
            print("Estamos sem estoque atualmente!")
            return []

    # Refactory:
    # 1, Adicionado o "return" dentro da método de verificação.
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível na lista de sabores."""
        if self.flavors:
            if flavor in self.flavors:
                return f"O sabor '{flavor}' está disponível no momento."
            else:
                return f"O sabor '{flavor}' não está disponível no momento."
        else:
            return "Estamos sem estoque atualmente."

    # Refactory:
    # 1. Adicionado o "return" dentro da método de verificação.
    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if self.open:
            if flavor in self.flavors:
                return f"O sabor '{flavor}' já está disponível no estoque."
            else:
                self.flavors.append(flavor)
                return f"O sabor '{flavor}' foi adicionado ao estoque."
        else:
            return "A sorveteria está fechada, não é possível adicionar sabores."
