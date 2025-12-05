from componente import Componente

class CaixaSelecao(Componente):
    """Representa um Checkbox."""

    def __init__(self, mediador):
        self.mediador = mediador
        self.marcado = False

    def marcar(self, valor: bool):
        self.marcado = valor
        self.mediador.notificar(self, "marcar")