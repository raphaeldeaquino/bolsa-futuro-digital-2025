from .forma import Forma

class Ponto(Forma):
    """
    Cada classe concreta de elemento deve implementar o método
    'aceitar' de tal maneira que ele chama o método visitante que
    corresponde com a classe do elemento.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def mover(self, x: float, y: float) -> None:
        self.x += x
        self.y += y

    def desenhar(self) -> None:
        print(f"Desenhando um ponto em ({self.x}, {self.y})")

    def aceitar(self, visitante) -> None:
        """
        Observe que nós estamos chamando `visitar_ponto`, que coincide
        com o nome da classe atual. Dessa forma nós permitimos
        que o visitante saiba a classe do elemento com o qual ele
        trabalha.
        """
        visitante.visitar_ponto(self)