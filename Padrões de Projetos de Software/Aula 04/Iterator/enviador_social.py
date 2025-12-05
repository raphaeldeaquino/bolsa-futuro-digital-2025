class EnviadorSocial:
    """
    Esta classe demonstra um truque útil:
    você pode passar um iterador para a classe cliente em vez de dar
    acesso direto à coleção completa. Assim, a coleção não é exposta.

    Outro benefício é que você pode alterar o modo como o cliente
    percorre a coleção em tempo de execução simplesmente passando
    um iterador diferente, já que o cliente não fica acoplado às
    classes concretas de iterador.
    """

    def enviar(self, iterador, mensagem):
        """
        Envia mensagens usando o iterador fornecido.
        """
        while iterador.ha_mais():
            perfil = iterador.proximo()
            self._enviar_email(perfil.obter_email(), mensagem)

    def _enviar_email(self, email, mensagem):
        """
        Método auxiliar para simular o envio de um e-mail.
        (No código real, isso chamaria um serviço externo.)
        """
        print(f"Enviando e-mail para {email}: {mensagem}")
