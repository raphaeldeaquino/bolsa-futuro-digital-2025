from abc import ABC, abstractmethod
from botao import Botao
from checkbox import Checkbox


# A interface fábrica abstrata declara um conjunto de métodos
# que retorna diferentes produtos abstratos. Estes produtos são
# chamados uma família e estão relacionados por um tema ou
# conceito de alto nível. Produtos de uma família são
# geralmente capazes de colaborar entre si. Uma família de
# produtos pode ter várias variantes, mas os produtos de uma
# variante são incompatíveis com os produtos de outro variante.
class GUIFactory(ABC):
    
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass
    
    @abstractmethod
    def criar_checkbox(self) -> Checkbox:
        pass