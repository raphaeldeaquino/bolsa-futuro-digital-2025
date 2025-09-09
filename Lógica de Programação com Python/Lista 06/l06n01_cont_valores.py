'''
Faça um algoritmo que carregue uma matriz 3 x 5 
com números inteiros, calcule e mostre a quantidade
de elementos entre 15 e 20.
'''

import random  # Importamos o módulo random para gerar números aleatórios

# Criamos uma lista vazia que será a matriz
matriz = []
# Definimos número de linhas e colunas
num_linhas = 3
num_colunas = 5
# Definimos o intervalo dos números aleatórios
valor_min = 1
valor_max = 30

# Inicializamos a matriz com zeros
for i in range(num_linhas):
    linha = [0] * num_colunas  # cria uma lista com 5 zeros
    matriz.append(linha)       # adiciona a linha na matriz

# Preenchemos a matriz com valores aleatórios inteiros entre 1 e 30
for i in range(num_linhas):          # percorre cada linha
    for j in range(num_colunas):     # percorre cada coluna da linha
        matriz[i][j] = random.randint(valor_min, valor_max)

# Inicializamos o contador
cont = 0
# Percorremos a matriz para contar quantos valores estão entre 15 e 20
for i in range(len(matriz)):         # percorre cada linha
    for j in range(len(matriz[i])):  # percorre cada elemento da linha
        if 15 <= matriz[i][j] <= 20: # verifica se o valor está no intervalo
            cont += 1                # incrementa o contador

# Exibimos a matriz completa
print(matriz)
# Exibimos a quantidade encontrada
print(f"Existem {cont} valores entre 15 e 20")
