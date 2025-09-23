# Importa a classe Produto definida em outro arquivo (Produto.py).
# Essa separação em módulos ajuda na organização do código.
from l02n05_Produto import Produto  

# Cria três instâncias da classe Produto.
# Cada uma receberá automaticamente um ID único, gerado pelo método de classe.
p1 = Produto()
p2 = Produto()
p3 = Produto()

# Imprime os produtos criados usando f-string.
# O método __str__ da classe Produto é chamado implicitamente,
# retornando uma representação amigável de cada objeto.
print(f"Produtos criados: {p1}, {p2} e {p3}")
