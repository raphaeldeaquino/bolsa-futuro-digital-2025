from abc import ABC, abstractmethod

class OuvinteEventos(ABC):
    """
    Interface do assinante.

    Se a linguagem suporta tipos funcionais, toda a hierarquia
    poderia ser substituída por funções — mas aqui usamos ABC.
    """

    @abstractmethod
    def atualizar(self, nome_arquivo):
        pass