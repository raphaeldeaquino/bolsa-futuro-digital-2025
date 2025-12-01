from tipo_arvore import TipoArvore

class FabricaArvore:
    """"
    A fábrica flyweight decide se reutiliza o flyweight existente
    ou cria um novo objeto.
    """

    tipos_arvore = []

    @staticmethod
    def get_tipo_arvore(nome: str, cor: str, textura: str) -> TipoArvore:
        # procura um TipoArvore existente
        for t in FabricaArvore.tipos_arvore:
            if t.nome == nome and t.cor == cor and t.textura == textura:
                return t

        # se não existir, cria e adiciona
        novo_tipo = TipoArvore(nome, cor, textura)
        FabricaArvore.tipos_arvore.append(novo_tipo)
        return novo_tipo
