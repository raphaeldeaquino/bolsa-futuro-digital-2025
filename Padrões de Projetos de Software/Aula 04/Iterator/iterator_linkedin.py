from iterator_perfil import IteradorPerfil

class IteratorLinkedin(IteradorPerfil):
    """
    Iterador concreto para percorrer perfis dentro do LinkedIn.
    """

    def __init__(self, linkedin, id_perfil, tipo):
        """
        O iterador precisa de uma referência para a coleção (LinkedIn)
        que será percorrida.

        Também armazena o estado da iteração independentemente de
        outros iteradores.
        """
        self.linkedin = linkedin
        self.id_perfil = id_perfil
        self.tipo = tipo

        self.posicao_atual = 0
        self.cache = None  # será preenchido sob demanda

    def _inicializar_preguicoso(self):
        """
        Inicializa o cache apenas quando necessário.
        """
        if self.cache is None:
            self.cache = self.linkedin.requisitar_grafo_social(self.id_perfil, self.tipo)

    def proximo(self):
        """
        Retorna o próximo Profile, se existir.
        """
        if self.ha_mais():
            resultado = self.cache[self.posicao_atual]
            self.posicao_atual += 1
            return resultado
        return None

    def ha_mais(self):
        """
        Retorna True se ainda houver perfis a iterar.
        """
        self._inicializar_preguicoso()
        return self.posicao_atual < len(self.cache)
