from circulo import Circulo
from elemento_grafico import ElementoGrafico
from elemento_grafico_composto import ElementoGraficoComposto
from ponto import Ponto

""""
O código cliente trabalha com todos os componentes através de
suas interfaces base. Dessa forma o código cliente pode
suportar componentes folha simples e composites complexos.
"""

todos = None
 
def carregar():
    todos = ElementoGraficoComposto()
    todos.adicionar(Ponto(1, 2))
    todos.adicionar(Circulo(5, 3, 10))

def agrupar_selecionados(componentes: []):
    grupo = ElementoGraficoComposto()
    for componente in componentes:
        grupo.adicionar(componente)
        todos.remover(componente)
    todos.adicionar(grupo)

    # Todos os componentes serão desenhados.
    todos.desenhar()

if __name__ == '__main__':
    carregar()
