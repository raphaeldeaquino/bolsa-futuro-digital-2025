from fonte_dados import FonteDados

class FonteDadosDecorator(FonteDados):
    """
    A classe decorador base segue a mesma interface que os outros
    componentes. O propósito primário dessa classe é definir a
    interface que envolve todos os decoradores concretos. A
    implementação padrão do código de envolvimento pode também
    incluir um campo para armazenar um componente envolvido e os
    meios para inicializá-lo.
    """

    def __init__(self, fonte: FonteDados):
        self.fonte = fonte

    def escrever_dados(self, dados):
        """"
        O decorador base simplesmente delega todo o trabalho para
        o componente envolvido. Comportamentos extra podem ser
        adicionados em decoradores concretos.
        """
        self.fonte.escrever_dados(dados)

    def ler_dados(self):
        """"
        Decoradores concretos podem chamar a implementação pai da
        operação ao invés de chamar o objeto envolvido
        diretamente. Essa abordagem simplifica a extensão de
        classes decorador.
        """
        return self.fonte.ler_dados()