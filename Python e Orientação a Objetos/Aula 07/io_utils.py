def escrever_arquivo(caminho, conteudo):
    # BUG: abre arquivo sem escrever (esqueceu f.write)
    f = open(caminho, "w")
    # BUG: deveria: f.write(conteudo)
    # esqueceu de escrever
    f.close()