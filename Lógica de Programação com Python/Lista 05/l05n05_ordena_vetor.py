'''
Escreva um programa que faça o mesmo procedimento do 
programa do exercício anterior para todos os
elementos do vetor.
'''

# Exemplos de entrada e o que acontece a cada passagem 

# [8 7 3 1 2] 1a posição com 2a posicao: 0 com 1 
# [7 8 3 1 2] 2a posição com 3a posicao: 1 com 2
# [7 3 8 1 2] 3a posição com 4a posicao: 2 com 3
# [7 3 1 8 2] 4a posição com 5a posicao: 3 com 4
# [7 3 1 2 8] ..., range(4) 

# [7 3 1 2 8] 1a posição com 2a posicao: 0 com 1 
# [3 7 1 2 8] 2a posição com 3a posicao: 1 com 2
# [3 1 7 2 8] 3a posição com 4a posicao: 2 com 3
# [3 1 2 7 8] ..., range(3)

# [3 1 2 7 8] 1a posição com 2a posicao: 0 com 1 
# [1 3 2 7 8] 2a posição com 3a posicao: 1 com 2
# [1 2 3 7 8] ..., range(2)

# [1 2 3 7 8] 1a posição com 2a posicao: 0 com 1 
# [1 2 3 7 8] ..., range(1)

'''
Código para fazer a leitura

vetor = [0] * 5
for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i + 1}o número: "))
'''

# Exemplo de vetor inicial
vetor = [5, 4, 3, 2, 1]

# O Bubble Sort precisa de várias "passadas"
# Cada passada empurra o maior número restante para o final do vetor.
# Por isso usamos um laço decrescente: na 1ª passada comparamos até o último índice,
# depois até o penúltimo, e assim por diante.

for limite in range(len(vetor) - 1, 0, -1):  
    # limite assume os valores [4, 3, 2, 1] para um vetor de tamanho 5
    print(f"\n--- Nova passada (limite = {limite}) ---")
    
    for i in range(limite):
        # Comparação entre elementos consecutivos
        print(f"Comparando posição {i} ({vetor[i]}) com posição {i+1} ({vetor[i+1]})")
        
        if vetor[i] > vetor[i + 1]:
            # Se o atual for maior que o próximo, trocamos de posição
            vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
            print(f"   Houve troca -> {vetor}")
        else:
            print(f"   Sem troca  -> {vetor}")

# Resultado final (vetor ordenado)
print("\nResultado final do Bubble Sort:")
print(vetor)
