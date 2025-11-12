from botao import Botao

# Produtos concretos são criados por fábricas concretas
# correspondentes.
class WinBotao(Botao):
    
    def desenhar(self) -> None:
        # Renderiza um botão no estilo Windows.
        print("Renderizando botão no estilo Windows")