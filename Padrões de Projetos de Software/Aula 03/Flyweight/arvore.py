from tipo_arvore import TipoArvore

class Arvore:
    """"
    O objeto contextual contém a parte extrínseca do estado da
    árvore. Uma aplicação pode criar bilhões desses estados, já
    que são muito pequenos:
    apenas dois números inteiros para coordenadas e um campo de
    referência.
    """

    def __init__(self, x: float, y: float, tipo_arvore: TipoArvore):
        self.x = x
        self.y = y
        self.tipo = tipo_arvore   # TipoArvore

    def draw(self, canvas: object) -> None:
        # delega o desenho para o TipoArvore
        self.tipo.desenhar(canvas, self.x, self.y)
