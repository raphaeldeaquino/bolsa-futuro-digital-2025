from Paciente import Paciente

class Medico:

    def __init__(self, nome: str, codigo: int, pacientes: list[Paciente]):
        self.nome = nome
        self.codigo = codigo
        self.pacientes = pacientes