from Paciente import Paciente

class Cliente:

    def __init__(self, nome: str, endereco: str, telefone: str, pacientes: list[Paciente]):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.pacientes = pacientes