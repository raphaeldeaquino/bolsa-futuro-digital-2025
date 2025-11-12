from aplicacao import Aplicacao
from mac_factory import MacFactory
from win_factory import WinFactory

# A aplicação seleciona o tipo de fábrica dependendo da atual
# configuração do ambiente e cria o widget no tempo de execução
# (geralmente no estágio de inicialização).
class ConfiguradorDaAplicacao:
    
    def ler_arquivo_configuracao_aplicacao(self) -> dict:
        # Simula leitura de arquivo de configuração
        return {"OS": "Mac"}  # Pode ser "Windows" ou "Mac"
    
    def main(self) -> None:
        config = self.ler_arquivo_configuracao_aplicacao()
        
        if config["OS"] == "Windows":
            factory = WinFactory()
        elif config["OS"] == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Erro! Sistema Operacional desconhecido.")
        
        app = Aplicacao(factory)
        app.criar_iu()
        app.desenhar()


# Exemplo de uso
if __name__ == "__main__":
    configurador = ConfiguradorDaAplicacao()
    configurador.main()