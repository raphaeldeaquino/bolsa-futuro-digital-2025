from gui_factory import GUIFactory
from button import Button
from checkbox import Checkbox
from win_button import WinButton
from win_checkbox import WinCheckbox

# As fábricas concretas produzem uma família de produtos que
# pertencem a uma única variante. A fábrica garante que os
# produtos resultantes sejam compatíveis. Assinaturas dos
# métodos fabrica retornam um produto abstrato, enquanto que
# dentro do método um produto concreto é instanciado.
class WinFactory(GUIFactory):
    
    def create_button(self) -> Button:
        return WinButton()
    
    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()