# Programa para calcular Y = X + 2X + 3X + ... + 20X

# Entrada de dados: leitura do valor de X
X = int(input("Digite um valor inteiro para X: "))

# Inicialização da variável que armazenará o resultado da soma
Y = 0

# Estrutura de repetição: multiplica X por cada valor de 1 até 20 e acumula na soma
for i in range(1, 21):  # range(1, 21) vai de 1 até 20 (inclusive)
    Y += i * X  # Soma o termo i*X ao valor acumulado

# Saída de dados: impressão do resultado final
print(f"O valor de Y é {Y}")
