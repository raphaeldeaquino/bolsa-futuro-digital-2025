from componente_com_ajuda_contextual import ComponenteComAjudaContextual

class Componente(ComponenteComAjudaContextual):
    """
    A classe base para componentes simples.
    """

    def __init__(self, texto_tooltip: str = None, container=None):
        self.texto_tooltip = texto_tooltip
        # O contêiner do componente age como o próximo elo na
        # corrente de handlers.
        self._container = container

    def mostrar_ajuda(self) -> None:
        """
        O componente mostra um tooltip (dica de contexto) se há
        algum texto de ajuda assinalado a ele. Do contrário ele
        passa a chamada adiante ao contêiner, se ele existir.
        """
        if self.texto_tooltip is not None:
            # Exibiria uma tooltip real em uma GUI;
            # aqui vamos simular com um print.
            print(f"Dica: {self.texto_tooltip}")
        else:
            if self._container is not None:
                self._container.mostrar_ajuda()
            else:
                print("Nenhuma ajuda disponível.")