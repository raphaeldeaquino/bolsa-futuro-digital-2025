from tv import TV
from radio import Radio
from controle_remoto import ControleRemoto
from controle_remoto_avancado import ControleRemotoAvancado

if __name__ == "__main__":
    tv = TV()
    controle = ControleRemoto(tv)
    controle.ligar_desligar()

    radio = Radio()
    controle_avancado = ControleRemotoAvancado(radio)
    controle_avancado.ligar_desligar()
    controle_avancado.aumentar_volume()