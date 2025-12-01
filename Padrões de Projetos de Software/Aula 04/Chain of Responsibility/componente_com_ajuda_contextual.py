from abc import ABC, abstractmethod

class ComponenteComAjudaContextual(ABC):
    """
    A interface do handler declara um método para executar um
    pedido.
    """
    
    @abstractmethod
    def mostrar_ajuda(self):
        pass
