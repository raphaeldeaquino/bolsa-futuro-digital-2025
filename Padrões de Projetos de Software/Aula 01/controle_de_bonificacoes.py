from funcionario import Funcionario

class ControleDeBonificacoes:
	 
    def __init__(self, total_de_bonificacoes: float=0):
         self.total_de_bonificacoes = total_de_bonificacoes

    def registra(self, funcionario: Funcionario):
         self.total_de_bonificacoes += funcionario.get_bonificacao()

    def get_total_de_bonificacoes(self):
         return self.total_de_bonificacoes