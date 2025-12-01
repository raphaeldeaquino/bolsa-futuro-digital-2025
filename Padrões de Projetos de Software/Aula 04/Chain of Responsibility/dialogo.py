from container import Container

class Dialogo(Container):
    """
    O mesmo que Painel
    """
    
    def __init__(self, url_pagina_wiki: str = None, texto_tooltip: str = None, container=None):
        super().__init__(texto_tooltip, container)
        self.url_pagina_wiki = url_pagina_wiki

    def mostrar_ajuda(self):
        if self.url_pagina_wiki is not None:
            # Aqui abriria a página do wiki de fato.
            # Para demonstração, apenas imprimimos.
            print(f"Abrindo página de ajuda: {self.url_pagina_wiki}")
        else:
            super().mostrar_ajuda()
