from fonte_dados_decorator import FonteDadosDecorator

class CompressaoDecorator(FonteDadosDecorator):
    """
    Você pode envolver objetos em diversas camadas de
    decoradores.
    """

    def escrever_dados(self, dados):
        """"
        1. Comprimir os dados passados.
        2. Passar os dados comprimidos para o método
        escrever_dados do objeto envolvido.
        """

    def ler_dados(self):
        """"
        1. Obter dados do método readData do objeto
        envolvido.
        2. Tentar descomprimi-lo se for comprimido.
        3. Retornar o resultado.
        """