from gui_factory import GUIFactory
from botao import Botao

# O código cliente trabalha com fábricas e produtos apenas
# através de tipos abstratos: GUIFactory, Button e Checkbox.
# Isso permite que você passe qualquer subclasse fábrica ou de
# produto para o código cliente sem quebrá-lo.
class Aplicacao:
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.botao: Botao = None
    
    def criar_iu(self) -> None:
        self.botao = self.factory.criar_botao()
    
    def desenhar(self) -> None:
        self.botao.desenhar()