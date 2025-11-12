from janela import Janela
from botao import Botao
from html_botao import HTMLBotao

# Criadores concretos sobrescrevem o método fábrica para mudar
# o tipo de produto resultante.
class WebJanela(Janela):
    
    def criar_botao(self) -> Botao:
        return HTMLBotao()
