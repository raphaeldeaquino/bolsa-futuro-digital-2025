from calc_basico import soma, subtrai, divide
import pytest

def test_soma_deveria_passar():
    assert soma(2, 3) == 5  # Esperado 5, mas soma retorna 6 -> FALHA

def test_subtrai_passando():
    assert subtrai(10, 3) == 7  # Deve passar

def test_divide_por_zero_deve_lancar():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)  # Espera ZeroDivisionError, mas função retorna None -> FALHA