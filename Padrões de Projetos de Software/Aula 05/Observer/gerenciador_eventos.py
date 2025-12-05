class GerenciadorEventos:
    """
    A classe publicadora base inclui o código de gerenciamento de
    inscrições e os métodos de notificação.
    """

    def __init__(self):
        self._ouvintes = {}  # mapa: tipo_evento -> lista de ouvintes

    def inscrever(self, tipo_evento, ouvinte):
        """Associa um ouvinte a um tipo de evento."""
        self._ouvintes.setdefault(tipo_evento, []).append(ouvinte)

    def desinscrever(self, tipo_evento, ouvinte):
        """Remove um ouvinte de um tipo de evento."""
        if tipo_evento in self._ouvintes:
            self._ouvintes[tipo_evento] = [
                o for o in self._ouvintes[tipo_evento] if o != ouvinte
            ]

    def notificar(self, tipo_evento, dados):
        """Notifica todos os ouvintes inscritos para o tipo de evento."""
        for ouvinte in self._ouvintes.get(tipo_evento, []):
            ouvinte.atualizar(dados)