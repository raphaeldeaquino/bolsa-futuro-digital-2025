from Prontuario import Prontuario

class Paciente:
    """
    Classe que representa um Paciente no sistema.

    Atributos:
        nome (str): Nome do paciente.
        raca (str): Raça ou grupo ao qual o paciente pertence.
        prontuario (Prontuario): Objeto que contém o prontuário do paciente.
    """

    def __init__(self, nome: str, raca: str, prontuario: Prontuario):
        """
        Inicializa um objeto Paciente com as informações fornecidas.

        Args:
            nome (str): Nome do paciente.
            raca (str): Raça ou grupo ao qual o paciente pertence.
            prontuario (Prontuario): Prontuário médico associado ao paciente.
        """
        self.nome = nome
        self.raca = raca
        self.prontuario = prontuario  # Boa prática: validar se é instância de Prontuario
