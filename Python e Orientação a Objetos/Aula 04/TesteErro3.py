class TesteErro3:
    @staticmethod
    def metodo1():
        print("inicio do metodo1")
        TesteErro3.metodo2()
        print("fim do metodo1")
 	
    @staticmethod
    def metodo2():
        print("inicio do metodo2");
        array = [0] * 10

        for i in range(15):
            try:
                array[i] = i
                print(i)
            except IndexError as e:
                print("erro: " + str(e))

        print("fim do metodo2")