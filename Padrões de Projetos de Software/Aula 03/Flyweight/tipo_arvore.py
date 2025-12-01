class TipoArvore:
    """"
    A classe flyweight contém uma parte do estado de uma árvore
    Esses campos armazenam valores que são únicos para cada
    árvore em particular. Por exemplo, você não vai encontrar
    coordenadas da árvore aqui. Já que esses dados geralmente são
    GRANDES, você gastaria muita memória mantendo-os em cada
    objeto árvore. Ao invés disso, nós podemos extrair a textura,
    cor e outros dados repetitivos em um objeto separado os quais
    muitas árvores individuais podem referenciar.
    """

    def __init__(self, nome: str, cor: str, textura: str):
        self.nome = nome
        self.cor = cor
        self.textura = textura

    def desenhar(self, canvas: object, x: float, y: float) -> None:
        """"
        1. Cria um bitmap de certo tipo, cor e textura.
        2. Desenha o bitmap em uma tela nas coordenadas X e Y.
        """
        pass