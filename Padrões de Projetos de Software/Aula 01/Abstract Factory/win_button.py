from button import Button

# Produtos concretos são criados por fábricas concretas
# correspondentes.
class WinButton(Button):
    
    def paint(self) -> None:
        # Renderiza um botão no estilo Windows.
        print("Renderizando botão no estilo Windows")