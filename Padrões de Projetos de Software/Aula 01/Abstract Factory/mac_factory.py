from gui_factory import GUIFactory
from button import Button
from checkbox import Checkbox
from mac_button import MacButton
from mac_checkbox import MacCheckbox

# Cada fábrica concreta tem uma variante de produto
# correspondente.
class MacFactory(GUIFactory):
    
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()