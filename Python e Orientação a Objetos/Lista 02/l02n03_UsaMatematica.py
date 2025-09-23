# Importa a classe Matematica definida em outro módulo (l02n03_Matematica.py).
# Isso ajuda na modularização do código, separando lógica matemática da interface com o usuário.
from l02n03_Matematica import Matematica  

# Solicita ao usuário a entrada de um número inteiro.
# O uso de int() garante que a entrada seja convertida para número.
num = int(input("Forneça um número: "))

# Chama o método estático da classe Matematica para verificar se o número é par.
num_par = Matematica.eh_par(num)

# Estrutura condicional para exibir o resultado ao usuário.
# A mensagem é construída com f-string, que é mais legível e eficiente.
if num_par:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
