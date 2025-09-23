class Matematica:
    """
    Classe utilitária para operações matemáticas.
    Métodos estáticos são usados porque não dependem do estado da instância.
    """

    @staticmethod
    def eh_par(numero: int) -> bool:
        """
        Verifica se um número é par, usando estrutura condicional explícita.

        Args:
            numero (int): Número inteiro a ser verificado.

        Returns:
            bool: True se o número for par, False caso contrário.
        """
        if numero % 2 == 0:
            return True
        else:
            return False

    @staticmethod 
    def eh_par_compacto(numero: int) -> bool:
        """
        Verifica se um número é par, de forma compacta.

        Args:
            numero (int): Número inteiro a ser verificado.

        Returns:
            bool: True se o número for par, False caso contrário.
        """
        # A expressão booleana já retorna True ou False diretamente
        return numero % 2 == 0
