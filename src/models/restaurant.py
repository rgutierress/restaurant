class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        # BUG 1: A primeira mensagem não retorna o nome do restaurante
        # Alterada a variavel self.cuisine_type para self.restaurant_name
        # Melhoria 1: Ajuste na mensagem and para e, mantendo o padrão português
        # Melhoria 2: Uso de dois prints para retornar a mensagem. Ajustado para um print inserindo quebra de linha
        # Melhoria 3: Inclusão da palavra culinária na frase
        # BUG 2: O metodo não estava retornando nenhuma string

        return f"Esse restaturante chama {self.restaurant_name} e serve culinária {self.cuisine_type}.\n Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        # BUG 1: Ambas as validações retornam o restaurante aberto
        # BUG 2: Acrescentado o return para as mensagens no método
        # BUG 3: Removido o método close_restaurant, pois foi ajustado um metodo para validar o status do restaurante
        # Removido a linha self.number_served = 0, pois não é utilizada no método

        if not self.open:
            self.open = True
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open == True:
            self.open = False
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        # BUG 1: Não estava retornando o numero de pessoas atendidas
        if self.isNumber(total_customers):
            return "Digite apenas números"
        else:
            if self.open:
                if total_customers < 0:
                    return "A quantidade de pessoas não pode ser menor que zero"
                else:
                    self.number_served = total_customers
                    return self.number_served
            else:
               return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # BUG 1: VALIDAÇÃO PARA STRING NÃO OCORRIA
        # BUG 2: QUANTIDADE DE PESSOAS NEGATIVO
        # BUG 3: NÃO RETORNAVA O NÚMERO DE PESSOAS ATENDIDAS
        # BUG 4: O INCREMENTO NÃO OCORRIA
        if self.isNumber(more_customers):
            return "Digite apenas números"
        else:
            if self.open:
                if more_customers < 0:
                    return "A quantidade de pessoas não pode ser menor que zero"
                else:
                    self.number_served += more_customers
                    return self.number_served
            else:
                return f"{self.restaurant_name} está fechado!"

    # Metodo para validar se o valor é uma string
    def isNumber(self, value):
        if isinstance(value,str):
            return True
        else:
            return False
