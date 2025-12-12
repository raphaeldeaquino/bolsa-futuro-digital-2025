from .visitante import Visitante

class VisitanteExportarXML(Visitante):
    """
    Visitantes concretos implementam várias versões do mesmo
    algoritmo, que pode trabalhar com todas as classes elemento
    concretas.

    Você pode usufruir do maior benefício do padrão Visitor
    quando estiver usando ele com uma estrutura de objeto
    complexa, tal como uma árvore composite. Neste caso, pode ser
    útil armazenar algum estado intermediário do algoritmo
    enquanto executa os métodos visitantes sobre vários objetos
    da estrutura.
    """
    def visitar_ponto(self, ponto) -> None:
        print(f"<Ponto x='{ponto.x}' y='{ponto.y}' />")

    def visitar_circulo(self, circulo) -> None:
        print(f"<Circulo x='{circulo.x}' y='{circulo.y}' raio='{circulo.raio}' />")

    def visitar_retangulo(self, retangulo) -> None:
        print(f"<Retangulo x='{retangulo.x}' y='{retangulo.y}' largura='{retangulo.largura}' altura='{retangulo.altura}' />")

    def visitar_forma_composta(self, forma_composta) -> None:
        print("<FormaComposta>")
        for forma in forma_composta.formas:
            forma.aceitar(self)
        print("</FormaComposta>")