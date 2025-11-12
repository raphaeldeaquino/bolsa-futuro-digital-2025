from botao import Botao

# Produtos concretos são criados por fábricas concretas
# correspondentes.
class MacBotao(Botao):
    
    def desenhar(self) -> None:
        # Renderiza um botão no estilo macOS.
        print("Renderizando botão no estilo macOS")