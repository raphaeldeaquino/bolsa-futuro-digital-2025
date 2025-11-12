from abc import ABC, abstractmethod


class Builder(ABC):
    """
    A interface builder especifica métodos para criar as
    diferentes partes de objetos produto.
    """

    @property
    @abstractmethod
    def produto(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_assentos(self) -> None:
        pass

    @abstractmethod
    def set_engine(self) -> None:
        pass

    @abstractmethod
    def set_computador_bordo(self) -> None:
        pass

    @abstractmethod
    def set_gps(self) -> None:
        pass