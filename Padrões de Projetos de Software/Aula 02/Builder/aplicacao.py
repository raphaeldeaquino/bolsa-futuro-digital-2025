from director import Director
from carro_builder import CarroBuilder

if __name__ == "__main__":
    """
    O código cliente cria um objeto builder, passa ele para o
    diretor e então inicia o processo de construção. O resultado
    final é recuperado do objeto builder.
    """

    director = Director()
    builder = CarroBuilder()
    director.builder = builder

    print("Carro básico: ")
    director.criar_carro_basico()
    builder.produto.list_parts()

    print("\n")

    print("Carro esportivo: ")
    director.criar_carro_esportivo()
    builder.produto.list_parts()
