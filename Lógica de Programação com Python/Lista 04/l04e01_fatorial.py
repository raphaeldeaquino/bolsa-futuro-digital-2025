# Programa para calcular o fatorial de um número inteiro N fornecido pelo usuário

# Entrada de dados: o usuário fornece um valor inteiro para N
N = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicialização da variável que armazenará o resultado do fatorial
# Começamos em 1 porque o fatorial é uma multiplicação e o elemento neutro da multiplicação é 1
fatorial = 1

# Estrutura de repetição: percorre os números de 1 até N (inclusive)
# A cada iteração, o valor de 'fatorial' é multiplicado pelo número atual do laço
for i in range(1, N + 1):
    fatorial *= i  # Multiplica o valor acumulado pelo número atual

# Saída de dados: impressão do resultado final
print(f"O fatorial de {N} é {fatorial}")
