from estado import Estado
from estado_bloqueado import EstadoBloqueado
from estado_pronto import EstadoPronto

class EstadoTocando(Estado):
    """
    Estado onde o tocador está reproduzindo uma música.
    """

    def clique_bloquear(self):
        self.player.alterar_estado(EstadoBloqueado(self.player))

    def clique_tocar(self):
        self.player.parar_reproducao()
        self.player.alterar_estado(EstadoPronto(self.player))

    def clique_proximo(self):
        """
        No pseudocódigo original havia um objeto 'event' com doubleclick.
        Como não há sistema de eventos, isto é um placeholder.
        """
        evento = {"duplo_clique": False}  # substituível conforme necessário

        if evento["duplo_clique"]:
            self.player.proxima_musica()
        else:
            self.player.avancar_rapido(5)

    def clique_anterior(self):
        evento = {"duplo_clique": False}

        if evento["duplo_clique"]:
            self.player.musica_anterior()
        else:
            self.player.retroceder(5)