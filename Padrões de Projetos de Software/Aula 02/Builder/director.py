from builder import Builder

class Director:
    """
    O diretor é apenas responsável por executar as etapas de
    construção em uma sequência em particular. Isso ajuda quando
    produzindo produtos de acordo com uma ordem específica ou
    configuração. A rigor, a classe diretor é opcional, já que o
    cliente pode controlar os builders diretamente.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        O diretor trabalha com qualquer instância builder que
        o código cliente passar a ele. Dessa forma, o código
        cliente pode alterar o tipo final do produto recém
        montado. O diretor pode construir diversas variações
        do produto usando as mesmas etapas de construção.
        """
        self._builder = builder

    def criar_carro_basico(self) -> None:
        self.builder.reset()
        self.builder.set_assentos()
        self.builder.set_engine()

    def criar_carro_esportivo(self) -> None:
        self.builder.reset()
        self.builder.set_assentos()
        self.builder.set_engine()
        self.builder.set_computador_bordo()
        self.builder.set_gps()