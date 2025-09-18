class Triangulo:
    """
    Classe que representa um triângulo geométrico básico.
    
    Atributos:
        base (float): Medida da base do triângulo.
        altura (float): Medida da altura do triângulo.
    
    Métodos:
        area(): Calcula a área do triângulo.
        perimetro(): Calcula o perímetro do triângulo (OBS: neste caso, a fórmula não é a correta para todos os triângulos).
        __str__(): Retorna uma representação textual do objeto.
    """

    def __init__(self, base: float, altura: float) -> None:
        """
        Inicializa um triângulo com base e altura.
        
        Args:
            base (float): Valor da base do triângulo.
            altura (float): Valor da altura do triângulo.
        """
        self.base = base
        self.altura = altura

    def area(self) -> float:
        """
        Calcula a área do triângulo.
        
        Returns:
            float: Área do triângulo.
        """
        return (self.base * self.altura) / 2
    
    def perimetro(self) -> float:
        """
        Calcula o perímetro do triângulo.
        
        OBS: A fórmula implementada ((base + altura) * 2) não corresponde ao perímetro
        de um triângulo genérico. Para o cálculo correto, seriam necessários
        os comprimentos dos três lados.
        
        Returns:
            float: Valor aproximado do perímetro (com a fórmula usada).
        """
        return (self.base + self.altura) * 2

    def __str__(self) -> str:
        """
        Retorna uma representação textual do triângulo.
        
        Returns:
            str: Representação contendo base e altura.
        """
        return f"Triângulo com base={self.base}, altura={self.altura}"
