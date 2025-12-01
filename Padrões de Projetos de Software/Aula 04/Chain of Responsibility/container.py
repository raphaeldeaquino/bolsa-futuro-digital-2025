from componente import Componente

class Container(Componente):
    """
    Contêineres podem conter tanto componentes simples como
    outros contêineres como filhos. As relações da corrente são
    definidas aqui. A classe herda o comportamento showHelp de
    sua mãe.
    """
    def __init__(self, texto_tooltip: str = None, container=None):
        super().__init__(texto_tooltip, container)
        self.filhos: list[Componente] = []

    def adicionar(self, filho: Componente):
        self.filhos.append(filho)
        filho.container = self