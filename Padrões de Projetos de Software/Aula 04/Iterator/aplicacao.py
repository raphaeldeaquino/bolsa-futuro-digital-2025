from enviador_social import EnviadorSocial
from facebook import Facebook
from linkedin import Linkedin

class Aplicacao:
    """
    A classe da aplicação configura coleções e iteradores e então
    os passa ao código cliente.
    """

    def __init__(self):
        self.rede = None
        self.enviador = None

    def configurar(self, usar_facebook=True):
        """
        Configura a rede social e o enviador de mensagens.
        """
        if usar_facebook:
            self.rede = Facebook()
        else:
            self.rede = Linkedin()

        self.enviador = EnviadorSocial()

    def enviar_spam_para_amigos(self, perfil):
        """
        Envia spam para os amigos do perfil informado.
        """
        iterador = self.rede.criar_iterador_amigos(perfil.obter_id())
        self.enviador.enviar(iterador, "Mensagem muito importante")

    def enviar_spam_para_colegas(self, perfil):
        """
        Envia spam para os colegas de trabalho do perfil informado.
        """
        iterador = self.rede.criar_iterador_colegas(perfil.obter_id())
        self.enviador.enviar(iterador, "Mensagem muito importante")
