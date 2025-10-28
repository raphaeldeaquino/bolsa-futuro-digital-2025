from button import Button

# Produtos concretos fornecem várias implementações da
# interface do produto.
class WindowsButton(Button):
    
    def render(self) -> None:
        # Renderiza um botão no estilo Windows.
        print("Renderizando botão Windows")
    
    def on_click(self, f) -> None:
        # Vincula um evento de clique do SO nativo.
        print("Vinculando evento de clique Windows")
        f()