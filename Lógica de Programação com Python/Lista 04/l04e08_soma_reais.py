# Programa para ler 200 valores reais e calcular o seu somatório

# Inicialização da variável que armazenará a soma
soma = 0.0

# Estrutura de repetição: lê 200 valores reais do usuário
for i in range(200):
    valor = float(input(f"Digite o {i+1}º valor real: "))  # leitura de um valor real
    soma += valor  # acumula o valor na soma

# Saída de dados: impressão do somatório final
print(f"O somatório dos 200 valores fornecidos é {soma}")
