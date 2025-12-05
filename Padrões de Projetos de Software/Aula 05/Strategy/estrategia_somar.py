from estrategia import Estrategia

class EstrategiaSomar(Estrategia):
    """
    Estratégias concretas implementam o algoritmo enquanto seguem
    a interface estratégia base. A interface faz delas
    intercomunicáveis no contexto.
    """

    def executar(self, a, b):
        return a + b