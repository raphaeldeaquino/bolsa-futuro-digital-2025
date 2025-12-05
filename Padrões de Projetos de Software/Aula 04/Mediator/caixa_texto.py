from componente import Componente

class CaixaTexto(Componente):
    """Representa um Textbox."""

    def __init__(self, mediador):
        self.mediador = mediador
        self.texto = ""