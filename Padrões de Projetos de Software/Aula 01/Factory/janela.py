from abc import ABC, abstractmethod
from botao import Botao


# A classe criadora declara o método fábrica que deve retornar
# um objeto de uma classe produto. As subclasses da criadora
# geralmente fornecem a implementação desse método.
class Janela(ABC):
    
    # A criadora também pode fornecer alguma implementação
    # padrão do Factory Method.
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    # Observe que, apesar do seu nome, a principal
    # responsabilidade da criadora não é criar produtos. Ela
    # geralmente contém alguma lógica de negócio central que
    # depende dos objetos produto retornados pelo método
    # fábrica. As subclasses pode mudar indiretamente essa
    # lógica de negócio ao sobrescreverem o método fábrica e
    # retornarem um tipo diferente de produto dele.
    def renderizar(self) -> None:
        # Chame o método fábrica para criar um objeto produto.
        ok_botao = self.criar_botao()
        # Agora use o produto.
        ok_botao.ao_clicar(self.fechar_janela)
        ok_botao.renderizar()
    
    def fechar_janela(self) -> None:
        print("Janela fechada")