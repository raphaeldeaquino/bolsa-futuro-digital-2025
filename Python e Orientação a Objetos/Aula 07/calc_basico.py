def soma(a, b):
    # BUG: implementado como multiplicação em vez de soma
    return a * b

def subtrai(a, b):
    return a - b

def divide(a, b):
    # BUG: silencia divisão por zero retornando None em vez de permitir a exceção
    try:
        return a / b
    except ZeroDivisionError:
        return None
