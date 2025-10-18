from io_utils import escrever_arquivo

def ler_arquivo(caminho):
    with open(caminho) as f:
        return f.read()

def test_escreve_e_ler(tmp_path):
    arq = tmp_path / "t.txt"
    escrever_arquivo(arq, "Olá pytest")
    assert ler_arquivo(arq) == "Olá pytest"  # FALHA: arquivo vazio