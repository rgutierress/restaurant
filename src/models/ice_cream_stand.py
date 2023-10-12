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
    # 1. Armazenamento de sabores disponíveis de forma separada e imprime diretamente.
    # 2. Valor de retorno imprime os sabores disponíveis e uma mensagem de estoque vazio.
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

    # Bug:
    # 1. Está imprimindo a lista completa de sabores disponíveis no qual deveria imprimir apenas o sabor informado em flavor
    # Refactory:
    # 1. Adição o "return" dentro do método de verificação.
    # 2. Substituíção de 'self.flavor' para 'flavor'.
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível na lista de sabores."""
        if self.flavors:
            if flavor in self.flavors:
                return f"O sabor '{flavor}' está disponível no momento."
            else:
                return f"O sabor '{flavor}' não está disponível no momento."
        else:
            return "Estamos sem estoque atualmente."

    #Bug:
    # 1. Estava imprimindo a lista completa de sabores em vez de apenas o sabor especificado.
    # Refactory:
    # 1. Substituíção de 'self.flavor' para 'flavor'.
    # 2. Adição o "return" dentro do método de verificação.
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
