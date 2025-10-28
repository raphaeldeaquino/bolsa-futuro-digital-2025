from button import Button

# Produtos concretos são criados por fábricas concretas
# correspondentes.
class MacButton(Button):
    
    def paint(self) -> None:
        # Renderiza um botão no estilo macOS.
        print("Renderizando botão no estilo macOS")