class Funcionario:
	 
    def __init__(self, nome: str, cpf: str, salario: float):
         self.nome = nome
         self.cpf = cpf
         self.salario = salario
         
    def get_bonificacao(self) -> float:
        return self.salario * 0.10

    # outros métodos aqui