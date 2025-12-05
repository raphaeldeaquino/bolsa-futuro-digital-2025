from iterator_perfil import IteradorPerfil

class IteratorFacebook(IteradorPerfil):
    """
    Iterador concreto para percorrer perfis dentro do Facebook.
    """

    def __init__(self, facebook, id_perfil, tipo):
        """
        O iterador precisa de uma referência para a coleção (Facebook)
        que será percorrida.

        Também armazena o estado da iteração independentemente de
        outros iteradores.
        """
        self.facebook = facebook
        self.id_perfil = id_perfil
        self.tipo = tipo

        self.posicao_atual = 0
        self.cache = None  # será preenchido sob demanda

    def _inicializar_preguicoso(self):
        """
        Inicializa o cache apenas quando necessário.
        """
        if self.cache is None:
            self.cache = self.facebook.requisitar_grafo_social(self.id_perfil, self.tipo)

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
