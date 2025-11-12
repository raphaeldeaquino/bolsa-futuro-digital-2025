from abc import ABC, abstractmethod

class Dispositivo(ABC):
    """"
    A interface "implementação" declara métodos comuns a todas as
    classes concretas de implementação. Ela não precisa coincidir
    com a interface de abstração. Na verdade, as duas interfaces
    podem ser inteiramente diferentes. Tipicamente a interface de
    implementação fornece apenas operações primitivas, enquanto
    que a abstração define operações de alto nível baseada
    naquelas primitivas.
    """

    @abstractmethod
    def esta_ligado(self) -> bool:
        pass

    @abstractmethod
    def ligar(self) -> None:
        pass

    @abstractmethod
    def desligar(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass

    @abstractmethod
    def get_canal(self) -> int:
        pass

    @abstractmethod
    def set_canal(self, canal: int) -> None:
        pass