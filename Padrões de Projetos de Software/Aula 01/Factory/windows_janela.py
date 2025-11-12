from janela import Janela
from botao import Botao
from windows_botao import WindowsBotao

# Criadores concretos sobrescrevem o método fábrica para mudar
# o tipo de produto resultante.
class WindowsJanela(Janela):
    
    def criar_botao(self) -> Botao:
        return WindowsBotao()