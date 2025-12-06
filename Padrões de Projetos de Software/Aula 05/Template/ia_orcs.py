from estrutura_fake import EstruturaFake
from ia_do_jogo import IAdoJogo
from inimigo_fake import InimigoFake

class IAOrcs(IAdoJogo):
    """
    Classes concretas têm que implementar todas as operações
    abstratas da classe base, mas não podem sobrescrever o método
    padrão em si.
    """

    def __init__(self):
        super().__init__()
        self.recursos = 30
        self.batedores = []
        self.guerreiros = []
        self.estruturas_construidas = [
            EstruturaFake("Fazenda"),
            EstruturaFake("Quartel")
        ]

    def construir_estruturas(self):
        print("[Orcs] Construindo estruturas...")
        if self.recursos > 0:
            """
            Construir fazendas, depois quartéis, e então uma fortaleza.
            """
            print("[Orcs] Construíram uma Fortaleza.")

    def construir_unidades(self):
        print("[Orcs] Construindo unidades...")
        if len(self.batedores) == 0:
            """
            Construir peão e adicionar ao grupo de batedores.
            """
            print("[Orcs] Construíram um Peão (batedor).")
            self.batedores.append("Peão")
        else:
            """
            Construir bruto e adicionar ao grupo de guerreiros.
            """
            print("[Orcs] Construíram um Bruto (guerreiro).")
            self.guerreiros.append("Bruto")

    def enviar_batedores(self, posicao):
        """
        Enviar batedores para a posição.
        """
        print(f"[Orcs] Batedores enviados para {posicao}.")

    def enviar_guerreiros(self, posicao):
        """
        Enviar guerreiros para a posição.
        """
        print(f"[Orcs] Guerreiros enviados para atacar em {posicao}.")

    def inimigo_mais_proximo(self):
        """
        Orcs sempre encontram um inimigo na simulação
        """
        return InimigoFake((10, 20))  