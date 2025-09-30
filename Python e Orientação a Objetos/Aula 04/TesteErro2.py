class TesteErro2:
    @staticmethod
    def metodo1():
        print("inicio do metodo1")
        TesteErro2.metodo2()
        print("fim do metodo1")
 	
    @staticmethod
    def metodo2():
        print("inicio do metodo2");
        array = [0] * 10

        try:
            for i in range(15):
                array[i] = i
                print(i)
        except IndexError as e:
            print("erro: " + str(e))

        print("fim do metodo2")