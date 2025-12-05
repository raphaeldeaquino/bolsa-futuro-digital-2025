class Componente:
    """
    Os componentes se comunicam com o mediador usando a interface do mediador.
    Graças a isso, você pode usar os mesmos componentes em outros contextos
    ao ligá-los com diferentes objetos mediadores.
    """

    def __init__(self, dialogo):
        """
        Construtor: recebe o mediador (dialogo) e armazena para futuras notificações.
        """
        self.dialogo = dialogo

    def clicar(self):
        """Envia uma notificação ao mediador indicando um clique."""
        self.dialogo.notificar(self, "clicar")

    def pressionar_tecla(self):
        """Envia uma notificação ao mediador indicando um pressionamento de tecla."""
        self.dialogo.notificar(self, "pressionar_tecla")
