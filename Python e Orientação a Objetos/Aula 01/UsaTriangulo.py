# Importa a classe Triangulo definida no módulo Triangulo.py
from Triangulo import Triangulo

# Cria um objeto Triangulo com base = 5 e altura = 10
t1 = Triangulo(5, 10)

# Cria um segundo objeto Triangulo com base = 2 e altura = 3
a = Triangulo(2, 3)

# Calcula e imprime a área de t1
print("Área de t1 = ", t1.area())

# Calcula e imprime o perímetro de t1
# OBS: A fórmula atual na classe não está correta para triângulos genéricos
print("Perímetro de t1 = ", t1.perimetro())

# Calcula e imprime a área do triângulo 'a'
print("Área de a = ", a.area())
