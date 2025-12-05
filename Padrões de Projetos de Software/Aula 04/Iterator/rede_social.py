class RedeSocial:
    """
    A interface da coleção deve declarar um método fábrica para
    produzir iteradores. Você pode declarar vários métodos se
    há diferentes tipos de iteração disponíveis no programa.
    """

    def criar_iterador_amigos(self, id_perfil):
        """Retorna um iterador para percorrer os amigos do perfil."""
        pass

    def criar_iterador_colegas(self, id_perfil):
        """Retorna um iterador para percorrer os colegas de trabalho do perfil."""
        pass
