from arvore import Arvore
from fabrica_arvore import FabricaArvore

class Floresta:
    """"
    As classes Árvore e Floresta são os clientes
    flyweight. Você pode uni-las se não planeja desenvolver mais
    a classe Arvore.
    """

    def __init__(self):
        self.arvores = []   # coleção de Arvores

    def plantar_arvore(self, x: float, y: float, nome: str, cor: str, textura: str) -> None:
        tipo_arvore = FabricaArvore.get_tipo_arvore(nome, cor, textura)
        arvore = Arvore(x, y, tipo_arvore)
        self.arvores.append(arvore)

    def desenhar(self, canvas):
        for arvore in self.arvores:
            arvore.desenhar(canvas)