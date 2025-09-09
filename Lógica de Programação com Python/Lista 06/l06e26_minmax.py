'''
Na teoria dos sistemas define-se o elemento 
MINMAX de uma matriz como sendo o maior elemento 
da linha onde se encontra o menor elemento da matriz. 
Faça um algoritmo que leia uma matriz 4 x 7 com 
números reais, calcule e mostre seu MINMAX e 
sua posição (linha e coluna).
'''
import random

# Criamos uma matriz vazia que será preenchida depois
matriz = []
# Definimos o número de linhas e colunas da matriz
num_linhas = 4
num_colunas = 7
# Definimos o intervalo dos valores aleatórios (de 0.0 a 10.0)
valor_min = 0.0
valor_max = 10.0

# Inicializamos a matriz com zeros
for i in range(num_linhas):
    # Criamos uma lista com 'num_colunas' elementos iguais a zero
    linha = [0] * num_colunas
    # Adicionamos essa linha dentro da matriz
    matriz.append(linha)

# Preenchemos a matriz com valores aleatórios reais
for i in range(num_linhas):
    for j in range(num_colunas):
        # Substituímos o zero por um número real entre valor_min e valor_max
        matriz[i][j] = random.uniform(valor_min, valor_max)

# Variáveis para encontrar o menor elemento da matriz
linha_do_menor = 0
# 'float('inf')' representa um valor infinito positivo (maior que qualquer número)
menor = float('inf')

# Procuramos o menor valor da matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_do_menor = i  # Guardamos a linha onde o menor valor foi encontrado

# Variáveis para encontrar o maior elemento da linha onde está o menor valor
# 'float('-inf')' representa um valor infinito negativo (menor que qualquer número)
maior = float('-inf')
coluna_do_maior = 0

# Procuramos o maior valor dentro da linha 'linha_do_menor'
for j in range(len(matriz[linha_do_menor])):
    if matriz[linha_do_menor][j] > maior:
        maior = matriz[linha_do_menor][j]
        coluna_do_maior = j  # Guardamos a coluna onde o maior valor foi encontrado

# Exibimos a matriz formatada (com duas casas decimais)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:.2f} ", end="")  # Mantém os valores da mesma linha juntos
    print("")  # Quebra a linha após imprimir cada linha da matriz

# Exibimos o resultado final (MINMAX e sua posição)
print(f"O MINMAX da matriz é {maior:.2f} na posição [{linha_do_menor},{coluna_do_maior}]")