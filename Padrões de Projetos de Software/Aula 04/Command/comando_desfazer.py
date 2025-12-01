from comando import Comando

class ComandoDesfazer(Comando):
    def executar(self) -> bool:
        # Apenas solicita ao aplicativo que desfaça o último comando.
        # Como não altera diretamente o editor, retorna False.
        self._app.desfazer()
        return False
