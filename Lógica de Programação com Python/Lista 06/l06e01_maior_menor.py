'''
Faça um algoritmo que carregue uma matriz 6 x 3, 
calcule e mostre:
• o maior elemento da matriz e sua respectiva posição, 
ou seja, linha e coluna;
• o menor elemento da matriz e sua respectiva posição, 
ou seja, linha e coluna.
'''

import random  # Para gerar valores aleatórios

# Criamos uma matriz vazia
matriz = []
# Definimos quantidade de turmas (linhas) e alunos por turma (colunas)
num_linhas = 6      # 6 turmas
num_colunas = 30    # 30 alunos por turma
# Definimos intervalo de notas (de 0.0 a 10.0)
valor_min = 0.0
valor_max = 10.0

# Inicializamos a matriz com zeros
for i in range(num_linhas):
    linha = [0] * num_colunas  # cria uma linha com 30 zeros
    matriz.append(linha)       # adiciona a linha na matriz

# Preenchemos a matriz com notas aleatórias reais (float)
for i in range(num_linhas):          # percorre cada turma
    for j in range(num_colunas):     # percorre cada aluno da turma
        matriz[i][j] = random.uniform(valor_min, valor_max)

# Inicializamos variáveis para guardar maior e menor nota
maior = 0.0
linha_do_maior = 0
coluna_do_maior = 0

menor = 10.0
linha_do_menor = 0
coluna_do_menor = 0

# Procuramos a maior e a menor nota dentro da matriz
for i in range(len(matriz)):          # percorre cada linha (turma)
    for j in range(len(matriz[i])):   # percorre cada coluna (aluno)
        # Verifica se encontramos uma nova maior nota
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_do_maior = i
            coluna_do_maior = j
        # Verifica se encontramos uma nova menor nota
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_do_menor = i
            coluna_do_menor = j

# Exibimos toda a matriz (todas as notas de todos os alunos)
print(matriz)

# Mostramos a maior nota encontrada e sua localização
print(f"A maior nota foi {maior:.2f}. "
      f"Foi obtida na turma {linha_do_maior + 1} pelo(a) aluno(a) {coluna_do_maior + 1}")

# Mostramos a menor nota encontrada e sua localização
print(f"A menor nota foi {menor:.2f}. "
      f"Foi obtida na turma {linha_do_menor + 1} pelo(a) aluno(a) {coluna_do_menor + 1}")
