import sieve

def test_sieve_of_eratosthenes():
    valor_esperado = [2, 3, 5, 7, 11]
    valor_retorno_atual = list(sieve.sieve_of_eratosthenes(12))
    assert valor_esperado == valor_retorno_atual