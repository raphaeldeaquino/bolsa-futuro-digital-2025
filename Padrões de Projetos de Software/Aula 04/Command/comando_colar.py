from comando import Comando

class ComandoColar(Comando):
    def executar(self) -> bool:
        # Como o comando altera o estado do editor, fazemos backup
        self.salvar_backup()

        # Substitui a seleção atual pelo conteúdo da área de transferência
        self._editor.substituir_selecao(self._app.area_de_transferencia)

        # Como altera o estado, deve retornar True para entrar no histórico
        return True
