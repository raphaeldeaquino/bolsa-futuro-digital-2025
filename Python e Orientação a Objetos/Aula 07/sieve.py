def sieve_of_eratosthenes(n):
    """
    Fornece todos os números primos de 1 a n
    """
    for i in range(n + 1):
        if e_primo(i):
            yield i

def e_primo(num):
    """
    Retorna True se o número for primo, caso contrário False
    """
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True