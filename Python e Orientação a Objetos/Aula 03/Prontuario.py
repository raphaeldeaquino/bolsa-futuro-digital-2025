class Prontuario:
    """
    Classe que representa o prontuário de um paciente.

    Atributos:
        exames (list[str]): Lista contendo os nomes dos exames realizados pelo paciente.
        descricao (str): Observações ou avaliação médica associada ao prontuário.
                        Por padrão, recebe o valor "Não avaliado".
    """

    def __init__(self, exames: list[str], descricao: str = "Não avaliado"):
        """
        Inicializa um objeto Prontuario.

        Args:
            exames (list[str]): Lista com os exames realizados.
            descricao (str, opcional): Descrição ou observações médicas.
                                       Valor padrão é "Não avaliado".
        """
        self.exames = exames
        self.descricao = descricao
