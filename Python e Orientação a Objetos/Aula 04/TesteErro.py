class TesteErro:
    @staticmethod
    def metodo1():
        print("inicio do metodo1")
        TesteErro.metodo2()
        print("fim do metodo1")
 	
    @staticmethod
    def metodo2():
        print("inicio do metodo2");
        array = [0] * 10
        for i in range(15):
            array[i] = i
            print(i)
 		
        print("fim do metodo2")