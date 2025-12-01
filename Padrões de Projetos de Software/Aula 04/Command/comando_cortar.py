from comando import Comando

class ComandoCortar(Comando):
    def executar(self) -> bool:
        # Como o comando altera o texto do editor, fazemos backup
        self.salvar_backup()

        # Copia a seleção para a área de transferência
        self._app.area_de_transferencia = self._editor.obter_selecao()

        # Remove a seleção do editor
        self._editor.deletar_selecao()

        # Retorna True para que seja registrado no histórico
        return True
