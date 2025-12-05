from editor import Editor
from ouvinte_email import OuvinteEmail
from ouvinte_log import OuvinteLog

class Aplicacao:
    """
    Uma aplicação pode configurar publicadores e assinantes
    durante o tempo de execução.
    """

    def configurar(self):
        editor = Editor()

        logger = OuvinteLog(
            "/tmp/log.txt",
            "Alguém abriu o arquivo: %s"
        )
        editor.eventos.inscrever("abrir", logger)

        alerta_email = OuvinteEmail(
            "admin@example.com",
            "Alguém alterou o arquivo: %s"
        )
        editor.eventos.inscrever("salvar", alerta_email)

        return editor  # útil para teste ou execução