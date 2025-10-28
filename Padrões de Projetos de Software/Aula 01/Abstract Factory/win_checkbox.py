from checkbox import Checkbox

class WinCheckbox(Checkbox):
    
    def paint(self) -> None:
        # Renderiza uma caixa de seleção estilo Windows.
        print("Renderizando checkbox no estilo Windows")