from contexto import Contexto
from estrategia_multiplicar import EstrategiaMultiplicar
from estrategia_somar import EstrategiaSomar
from estrategia_subtrair import EstrategiaSubtrair

class Aplicacao:
    """
    O código cliente escolhe uma estratégia concreta e passa ela
    para o contexto. O cliente deve estar ciente das diferenças
    entre as estratégia para que faça a escolha certa.
    """

    @staticmethod
    def main():
        print("Cria um objeto contexto.")
        contexto = Contexto()

        primeiro = int(input("Leia o primeiro número: "))
        segundo = int(input("Leia o segundo número: "))
        acao = input("Leia a ação desejada (somar, subtrair, multiplicar): ")

        if acao == "somar":
            contexto.definir_estrategia(EstrategiaSomar())
        elif acao == "subtrair":
            contexto.definir_estrategia(EstrategiaSubtrair())
        elif acao == "multiplicar":
            contexto.definir_estrategia(EstrategiaMultiplicar())
        else:
            raise ValueError("Ação desconhecida!")

        resultado = contexto.executar_estrategia(primeiro, segundo)
        print("Resultado:", resultado)


if __name__ == "__main__":
    Aplicacao.main()