from container import Container

class Painel(Container):
    """
    Mas componentes complexos podem sobrescrever a implementação
    padrão. Se o texto de ajuda não pode ser fornecido de uma
    nova maneira, o componente pode sempre chamar a implementação
    base (veja a classe Componente).
    """

    def __init__(self, texto_modal_ajuda: str = None, texto_tooltip: str = None, container=None):
        super().__init__(texto_tooltip, container)
        self.texto_modal_ajuda = texto_modal_ajuda

    def mostrar_ajuda(self):
        if self.texto_modal_ajuda is not None:
            # Aqui seria exibida uma janela modal real;
            # para fins de exemplo, usamos um print.
            print(f"Ajuda (modal): {self.texto_modal_ajuda}")
        else:
            super().mostrar_ajuda()
