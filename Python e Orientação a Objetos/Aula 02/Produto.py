class Produto:
    """
    Classe Produto que representa um item genérico.
    
    Atributos:
        contador (int): Atributo de classe que conta quantos objetos Produto foram criados.
        nome (str): Nome do produto.
        preco (float): Preço do produto.
    """
    
    # Atributo de classe (estático), compartilhado por todas as instâncias
    contador = 0

    def __init__(self, nome: str, preco: float):
        """
        Construtor da classe Produto.

        Parâmetros:
        nome (str): Nome do produto
        preco (float): Preço do produto
        """
        # Atributos de instância (cada objeto terá seus próprios valores)
        self.nome = nome
        self.preco = preco

        # Atualiza o contador de produtos criados (atributo de classe)
        Produto.contador += 1

    def __str__(self):
        """
        Retorna uma string com informações do produto.
        """
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"

    @classmethod
    def total_produtos(cls) -> int:
        """
        Método de classe que retorna o total de produtos criados.
        """
        return cls.contador
