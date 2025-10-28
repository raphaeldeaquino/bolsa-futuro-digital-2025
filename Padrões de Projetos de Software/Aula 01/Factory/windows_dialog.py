from dialog import Dialog
from button import Button
from windows_button import WindowsButton

# Criadores concretos sobrescrevem o método fábrica para mudar
# o tipo de produto resultante.
class WindowsDialog(Dialog):
    
    def create_button(self) -> Button:
        return WindowsButton()