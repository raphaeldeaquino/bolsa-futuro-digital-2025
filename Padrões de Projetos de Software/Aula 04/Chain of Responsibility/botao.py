from componente import Componente

class Botao(Componente):
    """
    Componentes primitivos estão de bom tamanho com a
    implementação de ajuda padrão.
    """

    def __init__(self, texto_tooltip: str = None, container=None):
        super().__init__(texto_tooltip, container)

    # O botão não precisa adicionar nada além do comportamento herdado.
    # Caso queira sobrescrever mostrar_ajuda(), basta implementar aqui.
