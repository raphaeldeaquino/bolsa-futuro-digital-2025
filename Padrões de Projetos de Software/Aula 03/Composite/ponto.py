from elemento_grafico import ElementoGrafico

class Ponto(ElementoGrafico):
    """"
    A classe folha representa objetos finais de uma composição.
    Um objeto folha não pode ter quaisquer sub-objetos.
    Geralmente, são os objetos folha que fazem o verdadeiro
    trabalho, enquanto que os objetos composite somente delegam
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def mover(self, x: float, y: float) -> None:
        self.x += x
        self.y += y

    def desenhar(self) -> None:
        # Desenhar um ponto em X e Y
        print(f"Ponto desenhado em ({self.x}, {self.y})")