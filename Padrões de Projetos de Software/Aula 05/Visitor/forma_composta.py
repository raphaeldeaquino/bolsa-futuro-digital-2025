from .forma import Forma

class FormaComposta(Forma):
    """
    Cada classe concreta de elemento deve implementar o método
    'aceitar' de tal maneira que ele chama o método visitante que
    corresponde com a classe do elemento.
    """

    def __init__(self) -> None:
        self.formas = []

    def adicionar_forma(self, forma: Forma) -> None:
        self.formas.append(forma)

    def mover(self, x: float, y: float) -> None:
        for forma in self.formas:
            forma.mover(x, y)

    def desenhar(self) -> None:
        print("Desenhando uma forma composta:")
        for forma in self.formas:
            forma.desenhar()

    def aceitar(self, visitante) -> None:
        """
        Observe que nós estamos chamando `visitar_forma_composta`, que coincide
        com o nome da classe atual. Dessa forma nós permitimos
        que o visitante saiba a classe do elemento com o qual ele
        trabalha.
        """
        visitante.visitar_forma_composta(self)