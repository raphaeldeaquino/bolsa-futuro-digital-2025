class BibliotecaYouTubeTerceirosImpl:
    """"
    A implementação concreta de um serviço conector. Métodos
    dessa classe podem pedir informações do YouTube. A velocidade
    do pedido depende da conexão do usuário com a internet, bem
    como do YouTube. A aplicação irá ficar lenta se muitos
    pedidos forem feitos ao mesmo tempo, mesmo que todos peçam a
    mesma informação.
    """
    
    def listar_videos(self):
        """
        Envia um pedido API para o YouTube.
        """
        pass

    def obter_informacoes_video(self, id_video):
        """
        Obtém metadados sobre algum vídeo.
        """
        pass

    def baixar_video(self, id_video):
        """
        Baixa um arquivo de vídeo do YouTube.
        """
        pass
