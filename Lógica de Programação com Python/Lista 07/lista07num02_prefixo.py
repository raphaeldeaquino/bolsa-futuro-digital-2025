def prefixo(string1: str, string2: str, ignore_maiusculo=True) -> bool:
    """
    Verifica se `string1` é prefixo de `string2`.

    Args:
        string1 (str): A string candidata a prefixo.
        string2 (str): A string na qual será verificado o prefixo.
        ignore_maiusculo (bool, opcional): Se True (padrão), ignora diferenças de maiúsculas/minúsculas
                                           na comparação. Se False, a comparação é sensível a maiúsculas.

    Returns:
        bool: True se `string1` for prefixo de `string2`, False caso contrário.

    Exemplos:
        >>> prefixo("Ana", "analfabeto")
        True
        >>> prefixo("Ana", "analfabeto", ignore_maiusculo=False)
        False
    """
    e_prefixo = False

    # Normaliza para minúsculas caso a comparação não deva diferenciar maiúsculas/minúsculas
    if ignore_maiusculo:
        string1 = string1.lower()
        string2 = string2.lower()

    # Só faz sentido verificar se a string candidata é prefixo se for menor ou igual à outra
    if len(string1) <= len(string2):
        e_prefixo = True  # assume que é prefixo, até que se prove o contrário

        # Percorre os caracteres de string1 e compara com os de string2
        for i in range(len(string1)):
            if string1[i] != string2[i]:  # encontrou um caractere diferente
                e_prefixo = False
                break  # não é mais necessário continuar a verificação

    return e_prefixo


# Exemplo de uso:
print(prefixo('Ana', 'analfabeto', ignore_maiusculo=False))
