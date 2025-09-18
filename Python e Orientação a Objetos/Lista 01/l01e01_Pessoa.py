class Pessoa:
    """
    Classe que representa uma pessoa.
    
    Atributos:
        nome (str): Nome da pessoa.
        numero_de_contribuinte (int): Número de identificação fiscal/contribuinte.
        idade (int): Idade da pessoa.
    """

    def __init__(self, nome: str = "", numero_de_contribuinte: int = 0, idade: int = 0) -> None:
        """
        Inicializa uma instância de Pessoa.
        
        Args:
            nome (str): Nome da pessoa.
            numero_de_contribuinte (int): Número fiscal. Deve ser não-negativo.
            idade (int): Idade em anos. Deve ser não-negativa.
        
        Raises:
            ValueError: Se idade ou numero_de_contribuinte forem negativos.
        """
        if numero_de_contribuinte < 0:
            raise ValueError("O número de contribuinte não pode ser negativo.")
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        
        self.nome = nome
        self.numero_de_contribuinte = numero_de_contribuinte
        self.idade = idade
    
    def __str__(self) -> str:
        """
        Retorna uma representação textual da pessoa.
        """
        return f"Nome: {self.nome}, Contribuinte: {self.numero_de_contribuinte}, Idade: {self.idade}"
