from estrategia import Estrategia

class Contexto:
    """
    O contexto define a interface de interesse para clientes.

    O contexto mantém uma referência para um dos objetos
    estratégia. O contexto não sabe a classe concreta de uma
    estratégia. Ele deve trabalhar com todas as estratégias
    através da interface estratégia.

    Geralmente o contexto aceita uma estratégia através do
    construtor, e também fornece um setter para que a
    estratégia possa ser trocada durante o tempo de execução.

    O contexto delega algum trabalho para o objeto estratégia
    ao invés de implementar múltiplas versões do algoritmo
    por conta própria.
    """

    def __init__(self, estrategia: Estrategia = None):
        self.estrategia = estrategia

    def definir_estrategia(self, estrategia: Estrategia):
        self.estrategia = estrategia

    def executar_estrategia(self, a: int, b: int):
        return self.estrategia.executar(a, b)


