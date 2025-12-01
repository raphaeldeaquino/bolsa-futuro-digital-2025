from conversor_video import ConversorVideo

if __name__ == '__main__':
    """"
    As classes da aplicação não dependem de um bilhão de classes
    fornecidas por um framework complexo. Também, se você decidir
    trocar de frameworks, você só precisa reescrever a classe
    fachada.
    """
    conversor = ConversorVideo()
    mp4 = conversor.converter("funny-cats-video.ogg", "mp4")
    mp4.salvar()