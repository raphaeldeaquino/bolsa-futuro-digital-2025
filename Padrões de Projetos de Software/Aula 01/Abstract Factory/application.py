from gui_factory import GUIFactory
from button import Button

# O código cliente trabalha com fábricas e produtos apenas
# através de tipos abstratos: GUIFactory, Button e Checkbox.
# Isso permite que você passe qualquer subclasse fábrica ou de
# produto para o código cliente sem quebrá-lo.
class Application:
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button: Button = None
    
    def create_ui(self) -> None:
        self.button = self.factory.create_button()
    
    def paint(self) -> None:
        self.button.paint()