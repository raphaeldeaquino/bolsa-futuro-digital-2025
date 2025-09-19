from Prontuario import Prontuario

class Paciente:

    def __init__(self, nome: str, raca: str, prontuario: Prontuario):
        self.nome = nome
        self.raca = raca
        self.prontuario = prontuario