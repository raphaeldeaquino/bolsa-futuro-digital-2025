from janela import Janela
from windows_janela import WindowsJanela
from web_janela import WebJanela

class Aplicacao:
    
    def __init__(self):
        self.janela: Janela = None
    
    # A aplicação seleciona um tipo de criador dependendo da
    # configuração atual ou definições de ambiente.
    def inicializar(self) -> None:
        config = self.ler_arquivo_configuracao_aplicacao()
        
        if config["OS"] == "Windows":
            self.janela = WindowsJanela()
        elif config["OS"] == "Web":
            self.janela = WebJanela()
        else:
            raise Exception("Error! Unknown operating system.")
    
    def ler_arquivo_configuracao_aplicacao(self) -> dict:
        # Simula leitura de arquivo de configuração
        return {"OS": "Web"}  # Pode ser "Windows" ou "Web"
    
    # O código cliente trabalha com uma instância de um criador
    # concreto, ainda que com sua interface base. Desde que o
    # cliente continue trabalhando com a criadora através da
    # interface base, você pode passar qualquer subclasse da
    # criadora.
    def main(self) -> None:
        self.inicializar()
        self.janela.renderizar()


# Exemplo de uso
if __name__ == "__main__":
    app = Aplicacao()
    app.main()