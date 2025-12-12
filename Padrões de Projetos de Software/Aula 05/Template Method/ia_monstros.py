from ia_do_jogo import IAdoJogo

class IAMonstros(IAdoJogo):
    """
    As subclasses também podem sobrescrever algumas operações com
    uma implementação padrão.
    """

    def coletar_recursos(self):
        """
        Monstros não coletam recursos.
        """
        print("[Monstros] Não coletam recursos.")

    def construir_estruturas(self):
        """
        Monstros não constroem estruturas.
        """
        print("[Monstros] Não constroem estruturas.")

    def construir_unidades(self):
        """
        Monstros não constroem unidades.
        """
        print("[Monstros] Não constroem unidades.")

    def enviar_batedores(self, posicao):
        """
        Monstros não têm batedores
        """
        print("[Monstros] Não possuem batedores.")

    def enviar_guerreiros(self, posicao):
        """
        Monstros não enviam guerreiros
        """
        print("[Monstros] Não realizam ataques organizados.")

    # Mantém inimigo = None → força o comportamento do algoritmo-padrão