from compressao_decorator import CompressaoDecorator
from criptografia_decorator import CriptografiaDecorator
from fonte_dados_arquivo import FonteDadosArquivo

if __name__ == '__main__':
    registros_salario = []
    fonte = FonteDadosArquivo("somefile.dat")
    fonte.escrever_dados(registros_salario)
    # O arquivo alvo foi escrito com dados simples.

    fonte = CompressaoDecorator(fonte)
    fonte.escrever_dados(registros_salario)
    # O arquivo alvo foi escrito com dados comprimidos.

    fonte = CriptografiaDecorator(fonte)
    # A variável fonte agora contém isso:
    # Encryption > Compression > FileDataSource
    fonte.escrever_dados(registros_salario)
    # O arquivo foi escrito com dados comprimidos e
    # encriptados.