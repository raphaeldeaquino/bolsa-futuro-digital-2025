from abc import ABC, abstractmethod
from .ponto import Ponto
from .circulo import Circulo
from .retangulo import Retangulo
from .forma_composta import FormaComposta

class Visitante(ABC):
    """
    A interface visitante declara um conjunto de métodos
    visitantes que correspondem com as classes elemento. A
    assinatura de um método visitante permite que o visitante
    identifique a classe exata do elemento com o qual ele está
    lidando.
    """

    @abstractmethod
    def visitar_ponto(self, ponto: Ponto) -> None:
        pass

    @abstractmethod
    def visitar_circulo(self, circulo: Circulo) -> None:
        pass

    @abstractmethod
    def visitar_retangulo(self, retangulo: Retangulo) -> None:
        pass

    @abstractmethod
    def visitar_forma_composta(self, forma_composta: FormaComposta) -> None:
        pass