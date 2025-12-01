from ponto import Ponto

class Circulo(Ponto):
    """"
    Todas as classes componente estendem outros componentes.
    """

    def __init__(self, x: float, y: float, raio: float):
        super().__init__(x, y)
        self.raio = raio
        
    def desenhar(self) -> None:
        # Desenhar um círculo em X e Y
        print(f"Círculo desenhado com centro em ({self.x}, {self.y}) e raio = {self.raio}")