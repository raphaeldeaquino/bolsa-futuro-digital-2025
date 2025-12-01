from comando import Comando
from comando_colar import ComandoColar
from comando_copiar import ComandoCopiar
from comando_cortar import ComandoCortar
from comando_desfazer import ComandoDesfazer
from editor import Editor
from historico_comandos import HistoricoComandos

class Aplicacao:
    def __init__(self):
        self.area_de_transferencia: str = ""
        self.editores: list[Editor] = []
        self.editor_ativo: Editor = None
        self.historico = HistoricoComandos()

    def criar_ui(self):
        # Exemplo ilustrativo — em uma aplicação real, 
        # haveria botões, atalhos etc.
        
        def copiar():
            self.executar_comando(
                ComandoCopiar(self, self.editor_ativo)
            )

        def cortar():
            self.executar_comando(
                ComandoCortar(self, self.editor_ativo)
            )

        def colar():
            self.executar_comando(
                ComandoColar(self, self.editor_ativo)
            )

        def desfazer():
            self.executar_comando(
                ComandoDesfazer(self, self.editor_ativo)
            )

        # Em uma interface real, ligaríamos:
        # botao_copiar.definir_acao(copiar)
        # atalhos.registrar("Ctrl+C", copiar)
        #
        # Aqui apenas armazeno para mostrar o conceito:
        self._acao_copiar = copiar
        self._acao_cortar = cortar
        self._acao_colar = colar
        self._acao_desfazer = desfazer

    def executar_comando(self, comando: Comando):
        """
        Executa um comando e, se ele alterou o estado,
        adiciona ao histórico.
        """
        if comando.executar():
            self.historico.empilhar(comando)

    def desfazer(self):
        """
        Desfaz o último comando usando o histórico.
        """
        comando = self.historico.desempilhar()
        if comando is not None:
            comando.desfazer()

