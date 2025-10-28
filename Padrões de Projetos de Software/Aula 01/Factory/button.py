from abc import ABC, abstractmethod

# A interface do produto declara as operações que todos os
# produtos concretos devem implementar.
class Button(ABC):
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def on_click(self, f) -> None:
        pass
