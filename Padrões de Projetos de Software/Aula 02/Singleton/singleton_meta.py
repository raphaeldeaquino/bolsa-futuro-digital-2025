class SingletonMeta(type):
    """
    A classe Singleton pode ser implementada de diferentes maneiras em Python. 
    Alguns métodos possíveis incluem: classe base, decorador e metaclasse. Usaremos a
    metaclasse porque ela é a mais adequada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possíveis alterações no valor do argumento `__init__` não afetam
        a instância retornada.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]