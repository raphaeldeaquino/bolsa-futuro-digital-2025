from pino_redondo import PinoRedondo

class BuracoRedondo():
    """"
    Digamos que você tenha duas classes com interfaces
    compatíveis: BuracoRedondo e PinoRedondo.
    """

    def __init__(self, raio: float):
        self.raio = raio

    def get_raio(self) -> float:
        """"
        Retorna o raio do buraco.
        """
        return self.raio

    def encaixa(self, pino: PinoRedondo) -> bool:
        return self.get_raio() >= pino.get_raio()