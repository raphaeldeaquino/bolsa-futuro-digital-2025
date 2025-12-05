class GerenciadorYouTube:
    """
    A classe GUI, que é usada para trabalhar diretamente com um
    objeto de serviço, permanece imutável desde que trabalhe com
    o objeto de serviço através de uma interface. Nós podemos
    passar um objeto proxy com segurança ao invés de um objeto
    real de serviço, uma vez que ambos implementam a mesma
    interface.
    """
    
    def __init__(self, servico):
        # Guarda a referência para o serviço (real ou proxy)
        self.servico = servico

    def renderizar_pagina_video(self, id_video):
        info = self.servico.obter_informacoes_video(id_video)
        # Renderiza a página do vídeo.
        # (conteúdo omitido propositalmente)

    def renderizar_painel_lista(self):
        lista = self.servico.listar_videos()
        # Renderiza a lista de miniaturas dos vídeos.
        # (conteúdo omitido propositalmente)

    def reagir_entrada_usuario(self):
        # Em um caso real, o ID do vídeo viria da interação do usuário
        self.renderizar_pagina_video(id_video=None)
        self.renderizar_painel_lista()
