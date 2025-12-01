from fonte_dados import FonteDados

class FonteDadosArquivo(FonteDados):
    """
    Componentes concretos fornecem uma implementação padrão para
    as operações. Pode haver diversas variações dessas classes em
    um programa.
    """

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def escrever_dados(self, dados):
        print("Escreve dados no arquivo")

    def ler_dados():
        print("Lê dados de um arquivo")