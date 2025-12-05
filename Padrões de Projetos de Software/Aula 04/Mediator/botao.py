from componente import Componente

class Botao(Componente):
    """Representa um Button."""

    def __init__(self, mediador):
        self.mediador = mediador

    def clicar(self):
        self.mediador.notificar(self, "clicar")