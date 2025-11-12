import math
from pino_redondo import PinoRedondo
from pino_quadrado import PinoQuadrado

class PinoQuadradoAdapter(PinoRedondo):
    """"
    Uma classe adaptadora permite que você encaixe pinos
    quadrados em buracos redondos. Ela estende a classe PinoRedondo
    para permitir que objetos do adaptador ajam como pinos
    redondos.
    """

    def __init__(self, pino: PinoQuadrado):
        """"
        Na verdade, o adaptador contém uma instância da classe
        PinoQuadrado.
        """
        self.pino = pino

    def get_raio(self):
        """"
        O adaptador finge que é um pino redondo com um raio
        que encaixaria o pino quadrado que o adaptador está
        envolvendo.
        """
        return self.pino.get_largura() * math.sqrt(2) / 2