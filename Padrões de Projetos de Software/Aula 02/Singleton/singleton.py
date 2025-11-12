from singleton_meta import SingletonMeta

class Singleton(metaclass=SingletonMeta):
    
    def alguma_logica_negocio(self):
        """
        Finalmente, qualquer singleton deve definir alguma lógica de negócio, que pode ser
        executada em sua instância.
        """
        pass