from abc import ABC, abstractmethod

class IteradorPerfil(ABC):
    """
    Interface comum a todos os iteradores de perfis.
    """

    @abstractmethod
    def proximo(self):
        """
        Retorna o próximo objeto Profile.
        """
        pass

    @abstractmethod
    def ha_mais(self):
        """
        Retorna True se ainda houver elementos a iterar.
        """
        pass
