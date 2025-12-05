from instantaneo import Instantaneo

class Editor:
    """
    O originador tem alguns dados importantes que podem mudar com
    o tempo. Ele também define um método para salvar seu estado
    dentro de um memento e outro método para restaurar o estado dele.
    """

    def __init__(self):
        self.texto = ""
        self.cursor_x = 0
        self.cursor_y = 0
        self.largura_selecao = 0

    def definir_texto(self, texto):
        """Define o texto do editor."""
        self.texto = texto

    def definir_cursor(self, x, y):
        """Define as coordenadas do cursor."""
        self.cursor_x = x
        self.cursor_y = y

    def definir_largura_selecao(self, largura):
        """Define a largura da seleção."""
        self.largura_selecao = largura

    def criar_instantaneo(self):
        """
        Salva o estado atual dentro de um memento.

        O memento é um objeto imutável; é por isso que o originador passa
        seu estado para os parâmetros do construtor do memento.
        """
        return Instantaneo(
            self,
            self.texto,
            self.cursor_x,
            self.cursor_y,
            self.largura_selecao
        )