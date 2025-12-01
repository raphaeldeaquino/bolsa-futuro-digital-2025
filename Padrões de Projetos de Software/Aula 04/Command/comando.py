from abc import ABC, abstractmethod

class Comando(ABC):
    """
    A classe comando base define a interface comum para todos
    comandos concretos.
    """

    def __init__(self, app, editor):
        self._app = app               
        self._editor = editor        
        self._backup = ""            

    def salvar_backup(self) -> None:
        """Faz backup do estado atual do editor."""
        self._backup = self._editor.texto

    def desfazer(self) -> None:
        """Restaura o estado salvo do editor."""
        self._editor.texto = self._backup

    @abstractmethod
    def executar(self) -> bool:
        """
        O método de execução é declarado abstrato para forçar
        todos os comandos concretos a fornecer suas próprias
        implementações. O método deve retornar verdadeiro ou
        falso dependendo se o comando muda o estado do editor.
        """
        pass
