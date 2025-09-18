def busca_sequencial(lista, chave, valor):
    """Realiza uma busca sequencial em uma lista de dicionários."""
    for item in lista:
        if str(item.get(chave)).lower() == str(valor).lower():
            return item
    return None

def busca_binaria(lista_ordenada, chave, valor):
    """
    Realiza uma busca binária em uma lista de dicionários.
    A lista DEVE estar pré-ordenada pela 'chave'.
    """
    baixo, alto = 0, len(lista_ordenada) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        valor_meio = lista_ordenada[meio].get(chave)

        # Trata comparação entre tipos diferentes (ex: str com int)
        try:
            if valor_meio < valor:
                baixo = meio + 1
            elif valor_meio > valor:
                alto = meio - 1
            else:
                return lista_ordenada[meio]
        except TypeError: # Se não for possível comparar diretamente
             if str(valor_meio).lower() < str(valor).lower():
                 baixo = meio + 1
             elif str(valor_meio).lower() > str(valor).lower():
                 alto = meio - 1
             else:
                 return lista_ordenada[meio]


    return None