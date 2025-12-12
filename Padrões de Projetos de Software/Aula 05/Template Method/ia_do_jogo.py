from abc import ABC, abstractmethod
from mapa_fake import MapaFake

class IAdoJogo(ABC):
    """
    A classe abstrata define um método padrão que contém um
    esqueleto de algum algoritmo composto de chamadas, geralmente
    para operações abstratas primitivas. Subclasses concretas
    implementam essas operações, mas deixam o método padrão em si
    intacto.
    """

    def __init__(self):
        self.estruturas_construidas = []
        self.mapa = MapaFake()

    def turno(self):
        """
        O método padrão define o esqueleto de um algoritmo.
        """
        print("\n=== INÍCIO DO TURNO ===")
        self.coletar_recursos()
        self.construir_estruturas()
        self.construir_unidades()
        self.atacar()
        print("=== FIM DO TURNO ===\n")

    def coletar_recursos(self):
        """
        Algumas das etapas serão implementadas diretamente na
        classe base.
        """
        print("[IA] Coletando recursos...")
        for estrutura in self.estruturas_construidas:
            estrutura.coletar()

    @abstractmethod
    def construir_estruturas(self):
        """
        Algumas etapas podem ser definidas como abstratas.
        """
        pass

    @abstractmethod
    def construir_unidades(self):
        pass

    def atacar(self):
        """
        Uma classe pode ter vários métodos padrão.
        """
        print("[IA] Fase de ataque...")
        inimigo = self.inimigo_mais_proximo()
        if inimigo is None:
            print("[IA] Nenhum inimigo encontrado. Enviando batedores para o centro do mapa.")
            self.enviar_batedores(self.mapa.centro)
        else:
            print(f"[IA] Inimigo encontrado em {inimigo.posicao}. Enviando guerreiros.")
            self.enviar_guerreiros(inimigo.posicao)

    def inimigo_mais_proximo(self):
        """
        Para a demonstração, cada IA decide diferente.
        Orcs: encontram inimigos
        Monstros: nunca encontram
        """
        return None  # padrão

    @abstractmethod
    def enviar_batedores(self, posicao):
        pass

    @abstractmethod
    def enviar_guerreiros(self, posicao):
        pass