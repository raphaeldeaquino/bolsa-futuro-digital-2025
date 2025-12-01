from comando import Comando

class ComandoCopiar(Comando):
    def executar(self) -> bool:
        # O comando copiar não modifica o texto do editor,
        # portanto não precisa salvar backup nem entrar no histórico.
        self._app.area_de_transferencia = self._editor.obter_selecao()
        return False
