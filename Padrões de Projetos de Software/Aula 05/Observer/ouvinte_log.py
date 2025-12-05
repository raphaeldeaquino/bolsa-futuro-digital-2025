from ouvinte_eventos import OuvinteEventos
from pathlib import Path

class OuvinteLog(OuvinteEventos):
    """
    Assinante que grava mensagens de log quando eventos ocorrem.
    """

    def __init__(self, caminho_log, mensagem):
        self._arquivo_log = Path(caminho_log)
        self._mensagem = mensagem

    def atualizar(self, nome_arquivo):
        mensagem_final = self._mensagem.replace("%s", nome_arquivo)
        with self._arquivo_log.open("a") as f:
            f.write(mensagem_final + "\n")