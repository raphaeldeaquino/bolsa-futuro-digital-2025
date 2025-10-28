from dialog import Dialog
from windows_dialog import WindowsDialog
from web_dialog import WebDialog

class Application:
    
    def __init__(self):
        self.dialog: Dialog = None
    
    # A aplicação seleciona um tipo de criador dependendo da
    # configuração atual ou definições de ambiente.
    def initialize(self) -> None:
        config = self.read_application_config_file()
        
        if config["OS"] == "Windows":
            self.dialog = WindowsDialog()
        elif config["OS"] == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system.")
    
    def read_application_config_file(self) -> dict:
        # Simula leitura de arquivo de configuração
        return {"OS": "Web"}  # Pode ser "Windows" ou "Web"
    
    # O código cliente trabalha com uma instância de um criador
    # concreto, ainda que com sua interface base. Desde que o
    # cliente continue trabalhando com a criadora através da
    # interface base, você pode passar qualquer subclasse da
    # criadora.
    def main(self) -> None:
        self.initialize()
        self.dialog.render()


# Exemplo de uso
if __name__ == "__main__":
    app = Application()
    app.main()