from gui_factory import GUIFactory
from botao import Botao
from checkbox import Checkbox
from mac_botao import MacBotao
from mac_checkbox import MacCheckbox

# Cada fábrica concreta tem uma variante de produto
# correspondente.
class MacFactory(GUIFactory):
    
    def criar_botao(self) -> Botao:
        return MacBotao()
    
    def criar_checkbox(self) -> Checkbox:
        return MacCheckbox()