from elemento_grafico import ElementoGrafico

class ElementoGraficoComposto(ElementoGrafico):
    """"
    A classe composite representa componentes complexos que podem
    ter filhos. Objetos composite geralmente delegam o verdadeiro
    trabalho para seus filhos e então "somam" o resultado.
    """

    def __init__(self):
        self.filhos = []

    def adicionar(self, filho: ElementoGrafico) -> None:
        """"
        Um objeto composite pode adicionar ou remover outros
        componentes (tanto simples como complexos) para ou de sua
        lista de filhos.
        """
        self.filhos.append(filho)

    def remover(self, filho: ElementoGrafico) -> None:
        self.filhos.remove(filho)
        
    def mover(self, x: float, y: float) -> None:
        """"
        Um composite executa sua lógica primária em uma forma
        particular. Ele percorre recursivamente através de todos
        seus filhos, coletando e somando seus resultados. Já que
        os filhos do composite passam essas chamadas para seus
        próprios filhos e assim em diante, toda a árvore de
        objetos é percorrida como resultado.
        """
        for filho in self.filhos:
            filho.mover(x, y)

    def desenhar(self) -> None:
        for filho in self.filhos:
            filho.desenhar()