from button import Button

# Produtos concretos fornecem várias implementações da
# interface do produto.
class HTMLButton(Button):
    
    def render(self) -> None:
        # Retorna uma representação HTML de um botão.
        print("Renderizando botão HTML")
    
    def on_click(self, f) -> None:
        # Vincula um evento de clique no navegador web.
        print("Vinculando evento de clique Web")
        f()