from abc import ABC, abstractmethod

# A interface do produto declara as operações que todos os
# produtos concretos devem implementar.
class Botao(ABC):
    
    @abstractmethod
    def renderizar(self) -> None:
        pass
    
    @abstractmethod
    def ao_clicar(self, f) -> None:
        pass
