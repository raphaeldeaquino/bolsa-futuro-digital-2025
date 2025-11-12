from abc import ABC, abstractmethod
from typing import Self


class Forma(ABC):
    
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        

    @abstractmethod
    def clone(self) -> Self:
        pass
