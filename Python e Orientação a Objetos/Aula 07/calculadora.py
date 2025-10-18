class Calculadora:
    def soma(self, a, b):
        return a + b

    def divide(self, a, b):
        # BUG: tenta forçar float mas usa abs() por engano
        if b == 0:
            raise ZeroDivisionError("divisão por zero")
        return abs(a) / abs(b)  # BUG: resultado errado para valores negativos