class Prontuario:

    def __init__(self, exames: list[str], descricao: str = "Não avaliado"):
        self.exames = exames
        self.descricao = descricao