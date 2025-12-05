from ouvinte_eventos import OuvinteEventos

class OuvinteEmail(OuvinteEventos):
    """
    Assinante que envia alertas por e-mail quando eventos ocorrem.
    (Simulado aqui com um print.)
    """

    def __init__(self, email, mensagem):
        self._email = email
        self._mensagem = mensagem

    def atualizar(self, nome_arquivo):
        mensagem_final = self._mensagem.replace("%s", nome_arquivo)
        # Simulação de envio de e-mail
        print(f"[EMAIL ENVIADO PARA {self._email}] {mensagem_final}")