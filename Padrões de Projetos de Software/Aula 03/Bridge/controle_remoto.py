from dispositivo import Dispositivo

class ControleRemoto:
    """"
    A "abstração" define a interface para a parte "controle" das
    duas hierarquias de classe. Ela mantém uma referência a um
    objeto da hierarquia de "implementação" e delega todo o
    trabalho real para esse objeto.
    """

    def __init__(self, dispositivo: Dispositivo):
        self.dispositivo = dispositivo
        
    def ligar_desligar(self) -> None:
        if self.dispositivo.esta_ligado():
            self.dispositivo.desligar()
        else:
            self.dispositivo.ligar()
           
    def diminuir_volume(self) -> None:
        self.dispositivo.set_volume(self.dispositivo.get_volume() - 10)

    def aumentar_volume(self) -> None:
        self.dispositivo.set_volume(self.dispositivo.get_volume() + 10)
    
    def proximo_canal(self) -> None:
        self.dispositivo.set_canal(self.dispositivo.get_canal() + 1)

    def canal_anterior(self) -> None:
        self.dispositivo.set_canal(self.dispositivo.get_canal() - 1)