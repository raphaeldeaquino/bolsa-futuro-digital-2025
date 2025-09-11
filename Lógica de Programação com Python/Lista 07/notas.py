import operacoes_matriz

# Gera uma matriz 6x10 com valores float aleatórios entre 0.0 e 10.0
matriz = operacoes_matriz.gera_matriz_aleatoria_float(6, 10, 0.0, 10.0)

# Inicialização dos valores de maior e menor, e suas respectivas posições
maior = 0.0
linha_do_maior = 0
coluna_do_maior = 0
menor = 10.0
linha_do_menor = 0
coluna_do_menor = 0

# Percorre todos os elementos da matriz
for i in range(len(matriz)):           # i percorre as linhas (turmas)
    for j in range(len(matriz[i])):    # j percorre as colunas (alunos)
        
        # Verifica se o valor atual é maior que o maior encontrado até agora
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_do_maior = i
            coluna_do_maior = j
        
        # Verifica se o valor atual é menor que o menor encontrado até agora
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            linha_do_menor = i
            coluna_do_menor = j

# Imprime a matriz completa
operacoes_matriz.imprime_matriz(matriz)

# Exibe a maior e menor nota, junto com suas posições (ajustadas para começar em 1)
print(f"A maior nota foi {maior:.2f}. "
      f"Foi obtida na turma {linha_do_maior + 1} pelo(a) aluno(a) {coluna_do_maior + 1}")

print(f"A menor nota foi {menor:.2f}. "
      f"Foi obtida na turma {linha_do_menor + 1} pelo(a) aluno(a) {coluna_do_menor + 1}")
