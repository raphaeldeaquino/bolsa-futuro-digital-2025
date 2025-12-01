from abc import ABC, abstractmethod

class FonteDados():
    """"
    A interface componente define operações que podem ser
    alteradas por decoradores.
    """

    @abstractmethod
    def escrever_dados(self, dados) -> None:
        pass


    @abstractmethod
    def ler_dados(self):
        pass