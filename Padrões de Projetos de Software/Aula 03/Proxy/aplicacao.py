from biblioteca_youtube_terceiros_impl import BibliotecaYouTubeTerceirosImpl
from biblioteca_youtube_com_cache import BibliotecaYouTubeComCache
from gerenciador_youtube import GerenciadorYouTube

class Aplicacao:
    """
    A aplicação pode configurar proxies de forma fácil e rápida.
    """
    def iniciar(self):
        servico_youtube = BibliotecaYouTubeTerceirosImpl()
        proxy_youtube = BibliotecaYouTubeComCache(servico_youtube)
        gerente = GerenciadorYouTube(proxy_youtube)
        gerente.reagir_entrada_usuario()


# Ponto de entrada principal da aplicação
if __name__ == "__main__":
    app = Aplicacao()
    app.iniciar()
