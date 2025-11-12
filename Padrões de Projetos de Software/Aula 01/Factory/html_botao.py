from botao import Botao

# Produtos concretos fornecem várias implementações da
# interface do produto.
class HTMLBotao(Botao):
    
    def renderizar(self) -> None:
        # Retorna uma representação HTML de um botão.
        print("Renderizando botão HTML")
    
    def ao_clicar(self, f) -> None:
        # Vincula um evento de clique no navegador web.
        print("Vinculando evento de clique Web")
        f()