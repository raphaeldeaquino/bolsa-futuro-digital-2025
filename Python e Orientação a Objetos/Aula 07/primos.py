def eh_primo(n):
    # BUG: trata 2 como não primo por usar <= em vez de <
    if n <= 2:
        return False
    
    for i in range(2, n-1):
        if n % i == 0:
            return False
    
    return True