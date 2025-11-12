from singleton import Singleton

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("O Singleton funciona, ambas as variáveis ​​contêm a mesma instância.")
    else:
        print("Falha no singleton, as variáveis ​​contêm instâncias diferentes.")