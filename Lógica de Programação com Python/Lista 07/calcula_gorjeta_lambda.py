# Define uma função tradicional que calcula 10% do valor da conta como gorjeta
def calcula_gorjeta(valor_conta):
    return valor_conta * 0.1  # Retorna 10% do valor da conta

# Redefine o nome calcula_gorjeta, agora como uma função anônima (lambda)
# Essa versão multiplica o valor da conta por 10, o que NÃO equivale a uma gorjeta,
# mas sobrescreve a função anterior
calcula_gorjeta = lambda valor_conta: valor_conta * 10
