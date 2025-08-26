# Programa para somar todos os números pares menores que 1000

# Inicialização da variável que armazenará o resultado da soma
soma = 0

# Estrutura de repetição: percorre todos os números de 2 até 999
# Usamos passo 2 para considerar apenas os pares
for i in range(2, 1000, 2):  
    soma += i  # Acumula o valor do número par na variável soma

# Saída de dados: impressão do resultado final
print(f"A soma dos números pares menores que 1000 é {soma}")
