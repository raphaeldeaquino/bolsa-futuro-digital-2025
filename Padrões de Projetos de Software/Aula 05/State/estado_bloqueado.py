from estado import Estado
from estado_pronto import EstadoPronto
from estado_tocando import EstadoTocando

class EstadoBloqueado(Estado):
    """
    Estado onde o tocador está bloqueado.
    """

    def clique_bloquear(self):
        """
        Quando você desbloqueia um tocador bloqueado, ele pode
        voltar para 'tocando' ou 'pronto'.
        """
        if getattr(self.player, "tocando", False):
            self.player.alterar_estado(EstadoTocando(self.player))
        else:
            self.player.alterar_estado(EstadoPronto(self.player))

    def clique_tocar(self):
        """Bloqueado — não faz nada."""
        pass

    def clique_proximo(self):
        """Bloqueado — não faz nada."""
        pass

    def clique_anterior(self):
        """Bloqueado — não faz nada."""
        pass