from controle_remoto import ControleRemoto

class ControleRemotoAvancado(ControleRemoto):
    """"
    Você pode estender classes a partir dessa hierarquia de
    abstração independentemente das classes de dispositivo.
    """

    def mutar(self) -> None:
        self.dispositivo.set_volume(0)