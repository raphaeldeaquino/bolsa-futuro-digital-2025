from arquivo_video import ArquivoVideo
from codec_factory import CodecFactory
from codec_compressao_mpeg import CodecCompressaoMPEG
from codec_compressao_ogg import CodecCompressaoOgg
from leitor_bitrate import LeitorBitrate

class ConversorVideo:
    """"
    Nós criamos uma classe fachada para esconder a complexidade
    do framework atrás de uma interface simples. É uma troca
    entre funcionalidade e simplicidade.
    """

    def converter(self, nome_arquivo: str, formato: str):
        arquivo = ArquivoVideo(nome_arquivo)
        codec_fonte = CodecFactory().extrair(arquivo)

        if formato == "mp4":
            codec_destino = CodecCompressaoMPEG()
        else:
            codec_destino = CodecCompressaoOgg()
        
        buffer = LeitorBitrate.ler(arquivo, codec_fonte)
        resultado = LeitorBitrate.converter(buffer, codec_destino)

        return resultado