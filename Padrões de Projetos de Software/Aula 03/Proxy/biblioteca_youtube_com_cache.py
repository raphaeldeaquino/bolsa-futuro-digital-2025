class BibliotecaYouTubeComCache:
    """
    Para salvar largura de banda, nós podemos colocar os
    resultados dos pedidos em cache e mantê-los por determinado
    tempo. Mas pode ser impossível colocar tal código diretamente
    na classe de serviço. Por exemplo, ela pode ter sido
    fornecida como parte de uma biblioteca de terceiros e/ou
    definida como final. É por isso que colocamos o código
    de cache em uma nova classe proxy que implementa a mesma
    interface que a classe de serviço. Ela delega ao objeto do
    serviço somente quando os pedidos reais precisam ser enviados.
    """
    
    def __init__(self, servico):
        # Referência ao serviço real
        self.servico = servico
        
        # Cache de lista de vídeos e informações de vídeos
        self.cache_lista = None
        self.cache_video = None
        
        # Flag para indicar se o cache precisa ser reiniciado
        self.precisa_reiniciar = False

    def listar_videos(self):
        if self.cache_lista is None or self.precisa_reiniciar:
            self.cache_lista = self.servico.listar_videos()
        return self.cache_lista

    def obter_informacoes_video(self, id_video):
        if self.cache_video is None or self.precisa_reiniciar:
            self.cache_video = self.servico.obter_informacoes_video(id_video)
        return self.cache_video

    def baixar_video(self, id_video):
        # Supondo que exista uma função auxiliar para verificar se o download já existe.
        if not self._download_existe(id_video) or self.precisa_reiniciar:
            self.servico.baixar_video(id_video)

    def _download_existe(self, id_video):
        """"
        Método auxiliar fictício apenas para manter a estrutura original do pseudocódigo.
        """
        # Aqui poderia haver lógica real, mas para fins de exemplo retornamos False.
        return False
