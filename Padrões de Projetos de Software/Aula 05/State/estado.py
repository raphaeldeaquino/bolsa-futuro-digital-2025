from abc import ABC, abstractmethod
from player_audio import PlayerAudio

class Estado(ABC):
    """
    Classe base dos estados. Declara métodos abstratos que todos
    os estados concretos precisam implementar e armazena uma referência
    para o contexto.
    """

    def __init__(self, player: PlayerAudio):
        """
        O contexto passa a si mesmo através do construtor do estado.
        Isso permite que o estado acesse dados ou altere o contexto.
        """
        self.player = player

    @abstractmethod
    def clique_bloquear(self):
        pass

    @abstractmethod
    def clique_tocar(self):
        pass

    @abstractmethod
    def clique_proximo(self):
        pass

    @abstractmethod
    def clique_anterior(self):
        pass