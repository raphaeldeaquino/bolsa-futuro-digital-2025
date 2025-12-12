class EstruturaFake:
    def __init__(self, nome):
        self.nome = nome

    def coletar(self):
        print(f"[Estrutura] {self.nome} coletou recursos.")