class Instantaneo:
    """
    A classe memento armazena o estado anterior do editor.
    """

    def __init__(self, editor, texto, cursor_x, cursor_y, largura_selecao):
        """
        Construtor: recebe o editor e uma cópia de seu estado atual.
        """
        self._editor = editor
        self._texto = texto
        self._cursor_x = cursor_x
        self._cursor_y = cursor_y
        self._largura_selecao = largura_selecao

    def restaurar(self):
        """
        Em algum momento, um estado anterior do editor pode ser
        restaurado usando um objeto memento.
        """
        self._editor.definir_texto(self._texto)
        self._editor.definir_cursor(self._cursor_x, self._cursor_y)
        self._editor.definir_largura_selecao(self._largura_selecao)