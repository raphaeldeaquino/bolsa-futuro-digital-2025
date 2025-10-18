import pytest
from primos import eh_primo

@pytest.mark.parametrize("n, esperado", [
    (2, True),   # 2 é primo — o código retorna False -> FALHA
    (3, True),
    (4, False),
    (17, True),
])

def test_primos(n, esperado):
    assert eh_primo(n) == esperado