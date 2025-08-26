# Programa para calcular a soma Y = (x+1) + (x+2) + (x+3) + ... + (x+100)

# Entrada de dados: leitura do valor de x
x = int(input("Digite um valor inteiro para x: "))

# Inicialização da variável que armazenará o resultado da soma
Y = 0

# Estrutura de repetição: soma todos os valores de (x+i), para i de 1 até 100
for i in range(1, 101):  # range(1, 101) vai de 1 até 100 (inclusivo)
    Y += (x + i)  # Acumula o valor de (x+i) em Y

# Saída de dados: impressão do resultado final
print(f"O valor de Y é {Y}")
