from comando import Comando

class HistoricoComandos:
    def __init__(self):
        self._historico: list[Comando] = []   # pilha de comandos

    def empilhar(self, comando: Comando):
        """Adiciona um comando ao topo da pilha."""
        self._historico.append(comando)

    def desempilhar(self) -> Comando:
        """Remove e retorna o comando mais recente."""
        if len(self._historico) == 0:
            return None
        return self._historico.pop()
