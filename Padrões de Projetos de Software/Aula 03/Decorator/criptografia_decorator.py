from fonte_dados_decorator import FonteDadosDecorator

class CriptografiaDecorator(FonteDadosDecorator):
    """
    Decoradores concretos devem chamar métodos no objeto
    envolvido, mas podem adicionar algo próprio para o resultado.
    Os decoradores podem executar o comportamento adicional tanto
    antes como depois da chamada ao objeto envolvido.
    """

    def escrever_dados(self, dados):
        """"
        1. Encriptar os dados passados.
        2. Passar dados encriptados para o método writeData
        do objeto envolvido.
        """

    def ler_dados(self):
        """"
        1. Obter os dados do método readData do objeto
        envolvido.
        2. Tentar decifrá-lo se for encriptado.
        3. Retornar o resultado.
        """