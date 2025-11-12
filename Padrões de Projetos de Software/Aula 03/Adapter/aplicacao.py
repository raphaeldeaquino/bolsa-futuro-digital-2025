from buraco_redondo import BuracoRedondo
from pino_redondo import PinoRedondo
from pino_quadrado import PinoQuadrado
from pino_quadrado_adapter import PinoQuadradoAdapter

if __name__ == "__main__":
    buraco = BuracoRedondo(5)
    pino_redondo = PinoRedondo(5)
    print(f"Pino redondo encaixa no buraco? {buraco.encaixa(pino_redondo)}")

    pino_quadrado_pequeno = PinoQuadrado(5)
    pino_quadrado_largo = PinoQuadrado(10)
    # Isso vai gerar exceção (tipos incompatíveis)
    try:
        print(f"Pino quadrado encaixa no buraco? {buraco.encaixa(pino_quadrado_pequeno)}")
        print(f"Pino quadrado encaixa no buraco? {buraco.encaixa(pino_quadrado_largo)}")
    except AttributeError:
        print("Gerou exceção")

    pino_quadrado_pequeno_adapter = PinoQuadradoAdapter(pino_quadrado_pequeno)
    pino_quadrado_largo_adapter = PinoQuadradoAdapter(pino_quadrado_largo)
    print(f"Pino quadrado encaixa no buraco? {buraco.encaixa(pino_quadrado_pequeno_adapter)}")
    print(f"Pino quadrado encaixa no buraco? {buraco.encaixa(pino_quadrado_largo_adapter)}")