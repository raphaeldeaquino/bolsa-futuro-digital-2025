from abc import ABC, abstractmethod
from button import Button


# A classe criadora declara o método fábrica que deve retornar
# um objeto de uma classe produto. As subclasses da criadora
# geralmente fornecem a implementação desse método.
class Dialog(ABC):
    
    # A criadora também pode fornecer alguma implementação
    # padrão do Factory Method.
    @abstractmethod
    def create_button(self) -> Button:
        pass

    # Observe que, apesar do seu nome, a principal
    # responsabilidade da criadora não é criar produtos. Ela
    # geralmente contém alguma lógica de negócio central que
    # depende dos objetos produto retornados pelo método
    # fábrica. As subclasses pode mudar indiretamente essa
    # lógica de negócio ao sobrescreverem o método fábrica e
    # retornarem um tipo diferente de produto dele.
    def render(self) -> None:
        # Chame o método fábrica para criar um objeto produto.
        ok_button = self.create_button()
        # Agora use o produto.
        ok_button.on_click(self.close_dialog)
        ok_button.render()
    
    def close_dialog(self) -> None:
        print("Dialog fechado")