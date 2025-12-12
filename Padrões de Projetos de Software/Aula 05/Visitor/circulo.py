from .forma import Forma

class Circulo(Forma):
    """
    Cada classe concreta de elemento deve implementar o método
    'aceitar' de tal maneira que ele chama o método visitante que
    corresponde com a classe do elemento.
    """

    def __init__(self, x: float, y: float, raio: float) -> None:
        self.x = x
        self.y = y
        self.raio = raio

    def mover(self, x: float, y: float) -> None:
        self.x += x
        self.y += y

    def desenhar(self) -> None:
        print(f"Desenhando um círculo em ({self.x}, {self.y}) com raio {self.raio}")

    def aceitar(self, visitante) -> None:
        """
        Observe que nós estamos chamando `visitar_circulo`, que coincide
        com o nome da classe atual. Dessa forma nós permitimos
        que o visitante saiba a classe do elemento com o qual ele
        trabalha.
        """
        visitante.visitar_circulo(self)