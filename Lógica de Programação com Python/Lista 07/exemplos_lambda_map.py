# Função lambda que multiplica dois números
multiplica = lambda num1, num2: num1 * num2

# Exemplo de uso da função multiplica
print(multiplica(2, 5))  # Saída: 10


# Função lambda que calcula o quadrado de um número
quadrado = lambda numero: numero * numero

# Lista de números de exemplo
lista = [2, 5, 6, 7, 8, 9, 15]

# Gerando manualmente uma lista com os números ao quadrado
lista_ao_quadrado = []
for i in range(len(lista)):
    lista_ao_quadrado.append(quadrado(lista[i]))

print(lista_ao_quadrado)  # Saída: [4, 25, 36, 49, 64, 81, 225]


# Usando a função map para aplicar 'quadrado' em todos os elementos da lista
lista_ao_quadrado = map(quadrado, lista)

# A função map retorna um iterador, por isso convertemos em lista para exibir o resultado
print(list(lista_ao_quadrado))  # Saída: [4, 25, 36, 49, 64, 81, 225]
