from dispositivo import Dispositivo

class TV(Dispositivo):
    """
    Classe concreta que implementa a interface Dispositivo.
    Representa uma televisão com estado interno de energia,
    volume e canal.
    """

    def __init__(self) -> None:
        self._ligado = False
        self._volume = 10   # volume inicial padrão
        self._canal = 1     # canal inicial padrão

    def esta_ligado(self) -> bool:
        return self._ligado

    def ligar(self) -> None:
        if not self._ligado:
            self._ligado = True
            print("A TV foi ligada.")
        else:
            print("A TV já está ligada.")

    def desligar(self) -> None:
        if self._ligado:
            self._ligado = False
            print("A TV foi desligada.")
        else:
            print("A TV já está desligada.")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        if 0 <= volume <= 100:
            self._volume = volume
            print(f"Volume ajustado para {self._volume}.")
        else:
            print("Valor de volume inválido. Deve estar entre 0 e 100.")

    def get_canal(self) -> int:
        return self._canal

    def set_canal(self, canal: int) -> None:
        if canal > 0:
            self._canal = canal
            print(f"Canal alterado para {self._canal}.")
        else:
            print("Canal inválido. Deve ser maior que zero.")
