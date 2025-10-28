from abc import ABC, abstractmethod

class Funcionario(ABC):
	 
    def __init__(self, nome: str, cpf: str, salario: float):
         self.nome = nome
         self.cpf = cpf
         self.salario = salario
         
    @abstractmethod
    def get_bonificacao(self) -> float:
        pass

    # outros métodos aqui