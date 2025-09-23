class Produto:
    """
    Classe que representa um produto com identificação única.
    Cada instância criada recebe um ID sequencial gerado automaticamente.
    """

    # Atributo de classe que mantém o contador de IDs.
    # É compartilhado entre todas as instâncias da classe.
    contador_ids = 0

    @classmethod
    def gerar_id(cls) -> int:
        """
        Gera um novo ID incremental para cada produto instanciado.

        Returns:
            int: O próximo ID disponível.
        """
        cls.contador_ids += 1
        return cls.contador_ids
    
    def __init__(self):
        """
        Inicializa um novo produto atribuindo automaticamente um ID único.
        """
        self.id = self.gerar_id()

    def __str__(self) -> str:
        """
        Retorna uma representação em string amigável para exibição do produto.

        Returns:
            str: Representação textual do produto.
        """
        return f"Produto id = {self.id}"
