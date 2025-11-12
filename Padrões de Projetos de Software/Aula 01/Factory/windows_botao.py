from botao import Botao

# Produtos concretos fornecem várias implementações da
# interface do produto.
class WindowsBotao(Botao):
    
    def renderizar(self) -> None:
        # Renderiza um botão no estilo Windows.
        print("Renderizando botão Windows")
    
    def ao_clicar(self, f) -> None:
        # Vincula um evento de clique do SO nativo.
        print("Vinculando evento de clique Windows")
        f()