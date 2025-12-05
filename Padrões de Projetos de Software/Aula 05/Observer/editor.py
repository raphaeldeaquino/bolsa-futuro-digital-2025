from gerenciador_eventos import GerenciadorEventos
from pathlib import Path

class Editor:
    """
    O publicador concreto contém a verdadeira lógica de negócio
    que é de interesse para alguns assinantes.

    O publicador é composto com um gerenciador de eventos para
    permitir o padrão Observer.
    """

    def __init__(self):
        self.eventos = GerenciadorEventos()
        self._arquivo = None

    def abrir_arquivo(self, caminho):
        """
        Métodos da lógica de negócio podem notificar assinantes
        acerca de mudanças.
        """
        self._arquivo = Path(caminho)
        self.eventos.notificar("abrir", self._arquivo.name)

    def salvar_arquivo(self):
        """Simula salvar e dispara notificação 'salvar'."""
        # Simulação de gravação
        if self._arquivo:
            self._arquivo.write_text("conteúdo modificado")
        self.eventos.notificar("salvar", self._arquivo.name)