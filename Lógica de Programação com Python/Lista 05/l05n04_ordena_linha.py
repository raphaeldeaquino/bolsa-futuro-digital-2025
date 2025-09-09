'''
Escreva um programa quer descubra qual é o maior elemento de um vetor e o coloque na última
posição do mesmo, comparando pares de elementos e permutando-os quando estiverem foram de
ordem
'''

# Exemplos de entrada e o que acontece a cada passagem 

# [8 7 3 1 2] 1a posição com 2a posicao: 0 com 1 
# tmp 8
# [7 8 3 1 2]
# [7 8 3 1 2] 2a posição com 3a posicao: 1 com 2
# [7 3 8 1 2] 3a posição com 4a posicao: 2 com 3
# [7 3 1 8 2] 4a posição com 5a posicao: 3 com 4
# [7 3 1 2 8]

# [3 7 8 1 2]
# [3 7 8 1 2]
# [3 7 8 1 2]
# [3 7 1 8 2]
# [3 7 1 2 8]

'''
Código para fazer a leitura

vetor = [0] * 5
for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite o {i + 1}o número: "))
'''

# Exemplo de vetor inicial (poderia ser digitado pelo usuário)
vetor = [8, 7, 3, 1, 2]

# O laço percorre todos os elementos do vetor, exceto o último
# porque sempre comparamos o elemento atual com o próximo (i com i+1).
for i in range(len(vetor) - 1):
    # Verificamos se o elemento atual é maior que o próximo
    if vetor[i] > vetor[i + 1]:
        # Se for maior, fazemos a troca de posições
        # A sintaxe 'a, b = b, a' troca os valores diretamente
        vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]

        # Exibimos o vetor após a troca, para acompanhar o processo
        print(f"Troca na posição {i} e {i+1}: {vetor}")
    else:
        # Se não houver troca, mostramos que os elementos já estavam na ordem correta
        print(f"Sem troca na posição {i} e {i+1}: {vetor}")

# Ao final dessa passada, o maior elemento foi "empurrado" para o final
print("\nResultado final após uma passada:")
print(vetor)