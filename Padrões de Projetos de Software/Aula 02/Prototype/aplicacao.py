from retangulo import Retangulo

if __name__ == '__main__':
    r1 = Retangulo(120, 250, 'blue', 10, 8)
    print(r1)
    r2 = r1.clone()
    print(r2)