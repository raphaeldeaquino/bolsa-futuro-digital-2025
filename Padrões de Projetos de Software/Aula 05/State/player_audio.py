from estado_pronto import EstadoPronto

class PlayerAudio:
    """
    A classe PlayerAudio age como um contexto. Ela também mantém
    uma referência para uma instância de uma das classes de
    estado que representa o estado atual do tocador de áudio.
    """

    def __init__(self):
        self.estado = EstadoPronto(self)

        # O contexto delega o manuseio das entradas do usuário
        # para um objeto de estado. O comportamento depende do estado.
        # A interface do usuário é omitida; aqui usamos métodos diretos.
        self.volume = 50
        self.playlist = []
        self.musica_atual = None

    # Outros objetos devem ser capazes de trocar o estado ativo do tocador.
    def alterar_estado(self, novo_estado):
        """Troca o estado ativo do tocador."""
        self.estado = novo_estado

    # Métodos chamados pela interface do usuário.
    def clique_bloquear(self):
        self.estado.clique_bloquear()

    def clique_tocar(self):
        self.estado.clique_tocar()

    def clique_proximo(self):
        self.estado.clique_proximo()

    def clique_anterior(self):
        self.estado.clique_anterior()

    # Métodos de serviço chamados pelos estados.
    def iniciar_reproducao(self):
        """Inicia a reprodução da música atual."""
        print("▶ Iniciando reprodução...")

    def parar_reproducao(self):
        """Para a reprodução."""
        print("⏹ Parando reprodução...")

    def proxima_musica(self):
        """Avança para a próxima música."""
        print("⏭ Próxima música")

    def musica_anterior(self):
        """Volta para a música anterior."""
        print("⏮ Música anterior")

    def avancar_rapido(self, tempo):
        """Avança rapidamente."""
        print(f"⏩ Avançando {tempo}s")

    def retroceder(self, tempo):
        """Retrocede rapidamente."""
        print(f"⏪ Retrocedendo {tempo}s")