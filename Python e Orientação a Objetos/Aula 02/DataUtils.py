from datetime import datetime

class DataUtils:
    """
    Classe utilitária para manipulação de datas.
    
    Contém métodos estáticos que podem ser usados sem criar uma instância da classe.
    """

    @staticmethod
    def validar_data(data_str: str) -> bool:
        """
        Verifica se uma string representa uma data válida no formato YYYY-MM-DD.
        
        Parâmetros:
            data_str (str): Data como string
        
        Retorna:
            bool: True se a data for válida, False caso contrário
        """
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def dias_entre_datas(data_inicio: str, data_fim: str) -> int:
        """
        Calcula a diferença em dias entre duas datas no formato YYYY-MM-DD.
        
        Parâmetros:
            data_inicio (str): Data inicial
            data_fim (str): Data final
        
        Retorna:
            int: Número de dias entre as datas
        """
        dt_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
        dt_fim = datetime.strptime(data_fim, "%Y-%m-%d")
        return (dt_fim - dt_inicio).days

    @staticmethod
    def hoje() -> str:
        """
        Retorna a data atual no formato YYYY-MM-DD.
        """
        return datetime.today().strftime("%Y-%m-%d")
