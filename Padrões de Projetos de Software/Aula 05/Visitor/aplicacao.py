from .ponto import Ponto
from .circulo import Circulo
from .retangulo import Retangulo
from .forma_composta import FormaComposta
from .visitante_exportar_xml import VisitanteExportarXML

def exportar_grafico():
    todas_as_formas = []

    ponto = Ponto(10, 20)
    todas_as_formas.append(ponto)

    circulo = Circulo(15, 25, 10)
    todas_as_formas.append(circulo)

    retangulo = Retangulo(5, 5, 20, 15)
    todas_as_formas.append(retangulo)

    forma_composta = FormaComposta()
    forma_composta.adicionar_forma(Ponto(1, 2))
    forma_composta.adicionar_forma(Circulo(3, 4, 5))
    todas_as_formas.append(forma_composta)

    for forma in todas_as_formas:
        forma.aceitar(VisitanteExportarXML())

if __name__ == "__main__":
    exportar_grafico()