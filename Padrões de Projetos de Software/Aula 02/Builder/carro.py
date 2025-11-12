from typing import Any

class Carro():
    """
    Faz sentido usar o padrão Builder somente quando seus produtos 
    são bastante complexos e exigem configuração extensa.

    Ao contrário de outros padrões de criação, diferentes builders 
    concretos podem produzir produtos não relacionados. Em outras palavras, 
    os resultados de vários builders podem nem sempre seguir a mesma interface.
    """

    def __init__(self) -> None:
        self.partes = []

    def adicionar(self, part: Any) -> None:
        self.partes.append(part)

    def list_parts(self) -> None:
        print(f"Partes do produto: {', '.join(self.partes)}", end="")