from abc import ABC, abstractmethod

class Forma(ABC):
    """
    O elemento interface declara um método `aceitar` que toma a
    interface do visitante base como um argumento.
    """

    @abstractmethod
    def mover(self, x: float, y: float) -> None:
        pass

    @abstractmethod
    def desenhar(self) -> None:
        pass

    @abstractmethod
    def aceitar(self, visitante) -> None:
        """
        Método de aceitação padrão que deve ser implementado por
        todas as classes concretas de elementos.
        """
        pass
