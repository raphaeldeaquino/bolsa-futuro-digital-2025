from abc import ABC, abstractmethod

# Cada produto distinto de uma família de produtos deve ter uma
# interface base. Todas as variantes do produto devem
# implementar essa interface.
class Botao(ABC):
    
    @abstractmethod
    def desenhar(self) -> None:
        pass