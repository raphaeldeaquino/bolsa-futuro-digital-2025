from abc import ABC, abstractmethod

# Aqui está a interface base de outro produto. Todos os
# produtos podem interagir entre si, mas a interação apropriada
# só é possível entre produtos da mesma variante concreta.
class Checkbox(ABC):
    
    @abstractmethod
    def paint(self) -> None:
        pass