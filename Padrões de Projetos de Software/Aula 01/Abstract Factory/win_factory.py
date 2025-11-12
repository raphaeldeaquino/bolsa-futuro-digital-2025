from gui_factory import GUIFactory
from botao import Botao
from checkbox import Checkbox
from win_botao import WinBotao
from win_checkbox import WinCheckbox

# As fábricas concretas produzem uma família de produtos que
# pertencem a uma única variante. A fábrica garante que os
# produtos resultantes sejam compatíveis. Assinaturas dos
# métodos fabrica retornam um produto abstrato, enquanto que
# dentro do método um produto concreto é instanciado.
class WinFactory(GUIFactory):
    
    def criar_botao(self) -> Botao:
        return WinBotao()
    
    def criar_checkbox(self) -> Checkbox:
        return WinCheckbox()