from Produto import Produto

# Criando objetos da classe Produto
p1 = Produto("Caneta", 2.5)
p2 = Produto("Caderno", 12.0)
p3 = Produto("Borracha", 1.5)

# Acessando informações individuais
print(p1.mostrar_info())  # Produto: Caneta, Preço: R$2.50
print(p2.mostrar_info())  # Produto: Caderno, Preço: R$12.00

# Consultando o total de produtos criados (atributo de classe)
print(f"Total de produtos criados: {Produto.total_produtos()}")
# Saída: Total de produtos criados: 3

# Observando que o contador é compartilhado por todas as instâncias
print(p1.contador, p2.contador, p3.contador)
# Saída: 3 3 3