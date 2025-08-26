# Programa para calcular A elevado a B (A^B), onde A e B são fornecidos pelo usuário

# Entrada de dados: o usuário fornece os valores de A (base) e B (expoente)
A = int(input("Digite o valor da base (A): "))
B = int(input("Digite o valor do expoente (B): "))

# Inicialização da variável que armazenará o resultado da potência
# Começamos em 1 porque qualquer número elevado a zero é igual a 1
resultado = 1

# Estrutura de repetição: multiplica a base A por ela mesma B vezes
# Se B for zero, o laço não executa e o resultado permanece 1 (corretamente, pois A^0 = 1)
for i in range(B):
    resultado *= A  # Multiplica o valor acumulado pela base

# Saída de dados: impressão do resultado final
print(f"O valor de {A} elevado a {B} é {resultado}")
