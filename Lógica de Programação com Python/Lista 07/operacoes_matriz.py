import random

def gera_matriz_aleatoria_float(num_linhas, num_colunas, valor_min, valor_max):
    """
    Gera uma matriz de números float aleatórios dentro de um intervalo.

    Args:
        num_linhas (int): Número de linhas da matriz.
        num_colunas (int): Número de colunas da matriz.
        valor_min (float): Valor mínimo possível.
        valor_max (float): Valor máximo possível.

    Returns:
        list[list[float]]: Matriz bidimensional com valores aleatórios.
    """
    matriz = []

    # Cria a estrutura inicial da matriz preenchida com zeros
    for i in range(num_linhas):
        linha = [0] * num_colunas
        matriz.append(linha)

    # Substitui os zeros por valores aleatórios de ponto flutuante
    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[i][j] = random.uniform(valor_min, valor_max)

    return matriz


def gera_matriz_aleatoria_int(num_linhas, num_colunas, valor_min, valor_max):
    """
    Gera uma matriz de números inteiros aleatórios dentro de um intervalo.

    Args:
        num_linhas (int): Número de linhas da matriz.
        num_colunas (int): Número de colunas da matriz.
        valor_min (int): Valor mínimo possível.
        valor_max (int): Valor máximo possível.

    Returns:
        list[list[int]]: Matriz bidimensional com valores aleatórios inteiros.
    """
    matriz = []

    # Cria a estrutura inicial da matriz preenchida com zeros
    for i in range(num_linhas):
        linha = [0] * num_colunas
        matriz.append(linha)

    # Substitui os zeros por valores aleatórios
    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[i][j] = random.int(valor_min, valor_max)

    return matriz


def imprime_matriz(matriz, casas_decimais=2):
    """
    Imprime a matriz formatada com número fixo de casas decimais.

    Args:
        matriz (list[list[float|int]]): Matriz a ser impressa.
        casas_decimais (int, opcional): Número de casas decimais para exibição. Padrão: 2.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:.{casas_decimais}f} ", end="")
        print("")  # quebra de linha a cada nova linha da matriz
