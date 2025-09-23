class Conversor:
    """
    Classe utilitária para conversões de unidades.
    Métodos estáticos são usados porque não dependem de atributos de instância.
    """

    @staticmethod
    def km_para_milhas(km: float) -> float:
        """
        Converte uma distância em quilômetros para milhas.

        Fórmula: milhas = km * 0.62137

        Args:
            km (float): Distância em quilômetros.

        Returns:
            float: Distância convertida em milhas.
        """
        return km * 0.62137
    
    @staticmethod
    def celsius_para_fahrenheit(c: float) -> float:
        """
        Converte uma temperatura em graus Celsius para Fahrenheit.

        Fórmula: F = C * 9/5 + 32

        Args:
            c (float): Temperatura em graus Celsius.

        Returns:
            float: Temperatura convertida em graus Fahrenheit.
        """
        return c * 9 / 5 + 32
