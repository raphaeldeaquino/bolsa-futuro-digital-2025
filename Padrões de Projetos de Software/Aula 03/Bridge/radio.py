from dispositivo import Dispositivo

class Radio(Dispositivo):
    """
    Classe concreta que implementa a interface Dispositivo.
    Representa um rádio com estado interno de energia,
    volume e frequência de estação.
    """

    def __init__(self) -> None:
        self._ligado = False
        self._volume = 5       # volume inicial padrão
        self._frequencia = 99.5  # frequência inicial (em MHz)

    def esta_ligado(self) -> bool:
        return self._ligado

    def ligar(self) -> None:
        if not self._ligado:
            self._ligado = True
            print("O rádio foi ligado.")
        else:
            print("O rádio já está ligado.")

    def desligar(self) -> None:
        if self._ligado:
            self._ligado = False
            print("O rádio foi desligado.")
        else:
            print("O rádio já está desligado.")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        if 0 <= volume <= 100:
            self._volume = volume
            print(f"Volume ajustado para {self._volume}.")
        else:
            print("Valor de volume inválido. Deve estar entre 0 e 100.")

    def get_canal(self) -> float:
        """Retorna a frequência atual (em MHz)."""
        return self._frequencia

    def set_canal(self, canal: float) -> None:
        """Define a frequência, assumindo faixa de 87.5 a 108.0 MHz."""
        if 87.5 <= canal <= 108.0:
            self._frequencia = canal
            print(f"Frequência ajustada para {self._frequencia} MHz.")
        else:
            print("Frequência inválida. Deve estar entre 87.5 e 108.0 MHz.")
