from ia_orcs import IAOrcs
from ia_monstros import IAMonstros

def simular():
    print("\n==============================")
    print("SIMULAÇÃO DO PADRÃO TEMPLATE METHOD")
    print("==============================\n")

    print(">>> IA: Orcs")
    orcs = IAOrcs()
    orcs.turno()

    print(">>> IA: Monstros")
    monstros = IAMonstros()
    monstros.turno()

if __name__ == "__main__":
    simular()