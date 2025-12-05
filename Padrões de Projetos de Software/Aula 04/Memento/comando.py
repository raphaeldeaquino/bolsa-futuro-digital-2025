class Comando:
    """
    Um objeto comando pode agir como cuidador. Neste caso, o
    comando obtém o memento antes que ele mude o estado do
    originador. Quando o desfazer (undo) é solicitado, ele
    restaura o estado do originador a partir de um memento.
    """

    def __init__(self, editor):
        self.editor = editor
        self.copia_seguro = None

    def criar_backup(self):
        """Cria um memento contendo o estado atual do editor."""
        self.copia_seguro = self.editor.criar_instantaneo()

    def desfazer(self):
        """Restaura o estado salvo caso exista um memento."""
        if self.copia_seguro is not None:
            self.copia_seguro.restaurar()