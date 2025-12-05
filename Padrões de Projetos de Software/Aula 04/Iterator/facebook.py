from iterator_facebook import IteratorFacebook
from rede_social import RedeSocial

class Facebook(RedeSocial):
    """
    Cada coleção concreta é acoplada a um conjunto de classes
    iteradoras concretas que ela retorna. Mas o cliente não é,
    pois a assinatura desses métodos retorna apenas interfaces
    de iterador.
    """

    # ...o grosso do código da coleção deve vir aqui...

    def criar_iterador_amigos(self, id_perfil):
        """
        Cria e retorna um iterador para percorrer os amigos do perfil.
        """
        return IteratorFacebook(self, id_perfil, "amigos")

    def criar_iterador_colegas(self, id_perfil):
        """
        Cria e retorna um iterador para percorrer os colegas de trabalho do perfil.
        """
        return IteratorFacebook(self, id_perfil, "colegas")
