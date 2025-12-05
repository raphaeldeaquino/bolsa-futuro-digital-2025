from abc import ABC, abstractmethod
from componente import Componente

class Mediador(ABC):
    """
    Interface do Mediador.

    Declara o método usado pelos componentes para notificar o mediador
    sobre diversos eventos. O mediador pode reagir a esses eventos
    e repassar a execução para outros componentes.
    """

    @abstractmethod
    def notificar(self, remetente: Componente, evento: str):
        """
        Notifica o mediador de que um componente disparou um evento.

        :param remetente: O componente que gerou o evento.
        :param evento: Nome do evento ocorrido.
        """
        pass
