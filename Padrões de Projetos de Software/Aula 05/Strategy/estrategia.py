from abc import ABC, abstractmethod

class Estrategia(ABC):
    """
    A interface estratégia declara operações comuns a todas as
    versões suportadas de algum algoritmo. O contexto usa essa
    interface para chamar o algoritmo definido pelas estratégias
    concretas.
    """

    @abstractmethod
    def executar(self, a, b):
        pass