from application import Application
from mac_factory import MacFactory
from win_factory import WinFactory

# A aplicação seleciona o tipo de fábrica dependendo da atual
# configuração do ambiente e cria o widget no tempo de execução
# (geralmente no estágio de inicialização).
class ApplicationConfigurator:
    
    def read_application_config_file(self) -> dict:
        # Simula leitura de arquivo de configuração
        return {"OS": "Mac"}  # Pode ser "Windows" ou "Mac"
    
    def main(self) -> None:
        config = self.read_application_config_file()
        
        if config["OS"] == "Windows":
            factory = WinFactory()
        elif config["OS"] == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")
        
        app = Application(factory)
        app.create_ui()
        app.paint()


# Exemplo de uso
if __name__ == "__main__":
    configurator = ApplicationConfigurator()
    configurator.main()