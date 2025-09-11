def calcula_gorjeta(valor_conta: float) -> float:
    """
    Calcula a gorjeta de 10% sobre o valor de uma conta.

    Args:
        valor_conta (float): Valor total da conta.

    Returns:
        float: Valor da gorjeta correspondente a 10% da conta.

    Exemplos:
        >>> calcula_gorjeta(100)
        10.0
        >>> calcula_gorjeta(137.5)
        13.75
    """
    return valor_conta * 0.1


# Exemplo de uso:
gorjeta = calcula_gorjeta(138.5) 
print(f"{gorjeta:.2f}")
