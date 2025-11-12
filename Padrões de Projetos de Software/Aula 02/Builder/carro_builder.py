from builder import Builder
from carro import Carro

class CarroBuilder(Builder):
    """
    As classes builder concretas seguem a interface do
    builder e fornecem implementações específicas das etapas
    de construção. Seu programa pode ter algumas variações de
    builders, cada uma implementada de forma diferente.
    """

    def __init__(self) -> None:
        """
        Uma instância fresca do builder deve conter um objeto
        produto em branco na qual ela usa para montagem futura.
        """
        self.reset()

    def reset(self) -> None:
        """"
        O método reset limpa o objeto sendo construído.
        """
        self._product = Carro()

    @property
    def produto(self) -> Carro:
        """
        Builders concretos devem fornecer seus próprios
        métodos para recuperar os resultados. Isso é porque
        vários tipos de builders podem criar produtos
        inteiramente diferentes que nem sempre seguem a mesma
        interface. Portanto, tais métodos não podem ser
        declarados na interface do builder (ao menos não em
        uma linguagem de programação de tipo estático).
    
        Geralmente, após retornar o resultado final para o
        cliente, espera-se que uma instância de builder comece
        a produzir outro produto. É por isso que é uma prática
        comum chamar o método reset no final do corpo do método
        `product`. Contudo este comportamento não é
        obrigatório, e você pode fazer seu builder esperar por
        uma chamada explícita do reset a partir do código cliente
        antes de se livrar de seu resultado anterior.
        """
        product = self._product
        self.reset()
        return product
    
    def set_assentos(self) -> None:
        """"
        Define o número de assentos no carro.
        """
        self._product.adicionar("Assentos")

    def set_engine(self) -> None:
        """"
        Instala um tipo de motor.
        """
        self._product.adicionar("Engine")

    def set_computador_bordo(self) -> None:
        """"
        Instala um computador de bordo.
        """
        self._product.adicionar("Computador de bordo")

    def set_gps(self) -> None:
        """"
        Instala um sistema de posicionamento global.
        """
        self._product.adicionar("GPS")