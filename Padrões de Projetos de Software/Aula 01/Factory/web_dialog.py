from dialog import Dialog
from button import Button
from html_button import HTMLButton

# Criadores concretos sobrescrevem o método fábrica para mudar
# o tipo de produto resultante.
class WebDialog(Dialog):
    
    def create_button(self) -> Button:
        return HTMLButton()
