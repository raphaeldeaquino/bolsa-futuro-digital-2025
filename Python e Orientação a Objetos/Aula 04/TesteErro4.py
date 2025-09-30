class TesteErro4:
    @staticmethod
    def metodo1():
        print("inicio do metodo1")
        try:
            TesteErro4.metodo2()
        except Exception as e:
            print("erro: " + str(e))
        print("fim do metodo1")
 	
    @staticmethod
    def metodo2():
        print("inicio do metodo2");
        array = [0] * 10

        for i in range(15):
            array[i] = i
            print(i)

        print("fim do metodo2")