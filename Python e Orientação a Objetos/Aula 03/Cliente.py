from Paciente import Paciente

class Cliente:
    """
    Classe que representa um Cliente no sistema.
    
    Atributos:
        nome (str): Nome do cliente.
        endereco (str): Endereço do cliente.
        telefone (str): Telefone de contato do cliente.
        pacientes (list[Paciente]): Lista de pacientes associados a este cliente.
    """

    def __init__(self, nome: str, endereco: str, telefone: str, pacientes: list[Paciente]):
        """
        Inicializa um objeto Cliente com as informações fornecidas.

        Args:
            nome (str): Nome do cliente.
            endereco (str): Endereço do cliente.
            telefone (str): Telefone de contato do cliente.
            pacientes (list[Paciente]): Lista de pacientes vinculados ao cliente.
        """
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.pacientes = pacientes  # Boa prática: validar se os itens da lista são instâncias de Paciente
