import copy
from forma import Forma

class Retangulo(Forma):

    def __init__(self, x, y, cor, largura, altura):
        super().__init__(x, y, cor)
        self.largura = largura
        self.altura = altura

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"<Retangulo: x={self.x}, y={self.y}, cor={self.cor}, largura={self.largura}, altura={self.altura}>"