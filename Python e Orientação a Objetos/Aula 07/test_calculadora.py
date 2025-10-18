import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_divide_positivos(calc):
    assert calc.divide(10, 2) == 5  # passa

def test_divide_negativo(calc):
    # Esperamos -5 mas implementação retorna 5 -> FALHA
    assert calc.divide(-10, 2) == -5