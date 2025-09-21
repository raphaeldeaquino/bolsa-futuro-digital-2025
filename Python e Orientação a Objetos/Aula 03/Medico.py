from Paciente import Paciente

class Medico:
    """
    Classe que representa um Médico no sistema.
    
    Atributos:
        nome (str): Nome completo do médico.
        codigo (int): Código identificador único do médico.
        pacientes (list[Paciente]): Lista de pacientes atendidos por este médico.
    """

    def __init__(self, nome: str, codigo: int, pacientes: list[Paciente]):
        """
        Inicializa um objeto Medico com os dados fornecidos.

        Args:
            nome (str): Nome completo do médico.
            codigo (int): Código identificador único do médico.
            pacientes (list[Paciente]): Lista de pacientes vinculados ao médico.
        """
        self.nome = nome
        self.codigo = codigo
        self.pacientes = pacientes  # Boa prática: validar se todos os itens são instâncias de Paciente
