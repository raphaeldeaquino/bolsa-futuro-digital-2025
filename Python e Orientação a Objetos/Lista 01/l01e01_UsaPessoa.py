from l01e01_Pessoa import Pessoa

# Cria uma pessoa informando todos os atributos
p1 = Pessoa("Joana", 456, 30)
print(f"p1 é igual: {p1}")

# Cria uma pessoa informando apenas o nome (os outros assumem os valores padrão definidos no construtor)
p2 = Pessoa("João")
print(f"p2 é igual: {p2}")

# Cria uma pessoa sem informar nada (tudo assume o valor padrão: nome="", contribuinte=0, idade=0)
p3 = Pessoa()
print(f"p3 é igual: {p3}")

# Cria uma pessoa informando apenas contribuinte e idade, usando argumentos nomeados
p4 = Pessoa(numero_de_contribuinte=789, idade=40)
print(f"p4 é igual: {p4}")
