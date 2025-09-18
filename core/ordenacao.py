def merge_sort(lista, chave):
    """Ordena uma lista de dicionários usando Merge Sort."""
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return _merge(esquerda, direita, chave)

def _merge(esquerda, direita, chave):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][chave] <= direita[j][chave]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, chave):
    """Ordena uma lista de dicionários usando Quick Sort."""
    if len(lista) <= 1:
        return lista
    
    copia_lista = list(lista) # Evita modificar a lista original

    pivo = copia_lista[len(copia_lista) // 2][chave]
    esquerda = [x for x in copia_lista if x[chave] < pivo]
    meio = [x for x in copia_lista if x[chave] == pivo]
    direita = [x for x in copia_lista if x[chave] > pivo]
    
    return quick_sort(esquerda, chave) + meio + quick_sort(direita, chave)