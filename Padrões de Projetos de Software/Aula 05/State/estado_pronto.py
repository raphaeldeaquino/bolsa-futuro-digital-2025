from estado import Estado
from estado_bloqueado import EstadoBloqueado
from estado_tocando import EstadoTocando

class EstadoPronto(Estado):
    """
    Estado onde o tocador está ligado, mas parado.
    """

    def clique_bloquear(self):
        self.player.alterar_estado(EstadoBloqueado(self.player))

    def clique_tocar(self):
        self.player.iniciar_reproducao()
        self.player.alterar_estado(EstadoTocando(self.player))

    def clique_proximo(self):
        self.player.proxima_musica()

    def clique_anterior(self):
        self.player.musica_anterior()