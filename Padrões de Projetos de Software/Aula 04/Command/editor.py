class Editor:
    """
    A classe do editor tem verdadeiras operações de edição de
    texto. Ela faz o papel de destinatária: todos os comandos
    acabam delegando a execução para os métodos do editor.
    """
    
    def __init__(self):
        self.texto = ""
        self._inicio_selecao = 0
        self._fim_selecao = 0

    def definir_selecao(self, inicio: int, fim: int):
        """Define a seleção atual no texto."""
        self._inicio_selecao = max(0, min(inicio, len(self.texto)))
        self._fim_selecao = max(0, min(fim, len(self.texto)))

    def obter_selecao(self) -> str:
        """Retorna o texto selecionado."""
        return self.texto[self._inicio_selecao:self._fim_selecao]

    def deletar_selecao(self):
        """Remove o texto selecionado."""
        antes = self.texto[:self._inicio_selecao]
        depois = self.texto[self._fim_selecao:]
        self.texto = antes + depois

        # Depois de deletar, a seleção colapsa no ponto inicial
        self._fim_selecao = self._inicio_selecao

    def substituir_selecao(self, novo_texto: str):
        """Substitui a seleção atual pelo texto fornecido."""
        antes = self.texto[:self._inicio_selecao]
        depois = self.texto[self._fim_selecao:]
        self.texto = antes + novo_texto + depois

        # A seleção passa a ser o texto colado
        nova_posicao = self._inicio_selecao + len(novo_texto)
        self._inicio_selecao = nova_posicao
        self._fim_selecao = nova_posicao
