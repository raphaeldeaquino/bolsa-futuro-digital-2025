from abc import ABC, abstractmethod

class ElementoGrafico(ABC):
    """"
    A interface componente declara operações comuns para ambos os
    objetos simples e complexos de uma composição.
    """

    @abstractmethod
    def mover(self, x: float, y: float) -> None:
        pass

    @abstractmethod
    def desenhar(self) -> None:
        pass