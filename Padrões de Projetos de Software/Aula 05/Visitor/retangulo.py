from .forma import Forma

class Retangulo(Forma):
    """
    Cada classe concreta de elemento deve implementar o método
    'aceitar' de tal maneira que ele chama o método visitante que
    corresponde com a classe do elemento.
    """

    def __init__(self, x: float, y: float, largura: float, altura: float) -> None:
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def mover(self, x: float, y: float) -> None:
        self.x += x
        self.y += y

    def desenhar(self) -> None:
        print(f"Desenhando um retângulo em ({self.x}, {self.y}) com largura {self.largura} e altura {self.altura}")

    def aceitar(self, visitante) -> None:
        """
        Observe que nós estamos chamando `visitar_retangulo`, que coincide
        com o nome da classe atual. Dessa forma nós permitimos
        que o visitante saiba a classe do elemento com o qual ele
        trabalha.
        """
        visitante.visitar_retangulo(self)