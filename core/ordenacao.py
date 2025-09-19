def _merge(esquerda, direita, chave):
    """Função auxiliar para mesclar duas listas ordenadas."""
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


def merge_sort(lista, chave):
    """Ordena uma lista de dicionários usando Merge Sort.

    Complexidade: O(n log n), onde n é o tamanho da lista.
    """
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return _merge(esquerda, direita, chave)


def quick_sort(lista, chave):
    """Ordena uma lista de dicionários usando Quick Sort.
    PS: Usa Out-of-Place Quick Sort para simplicidade, porém consome mais memória.

    Complexidade: O(n log n) em média, O(n^2) no pior caso, onde n é o tamanho da lista.
    """
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2][chave]
    esquerda = [x for x in lista if x[chave] < pivo]
    meio = [x for x in lista if x[chave] == pivo]
    direita = [x for x in lista if x[chave] > pivo]

    return quick_sort(esquerda, chave) + meio + quick_sort(direita, chave)


if __name__ == "__main__":
    dados_teste = [
        {
            "nome_insumo": "Reagente A",
            "quantidade_consumida": 50,
            "validade": "2024-12-31",
        },
        {
            "nome_insumo": "Reagente B",
            "quantidade_consumida": 20,
            "validade": "2023-11-30",
        },
        {
            "nome_insumo": "Reagente C",
            "quantidade_consumida": 75,
            "validade": "2025-01-15",
        },
    ]

    print("Dados Originais:")
    for item in dados_teste:
        print(item)

    print("\nOrdenado por Quantidade Consumida (Merge Sort):")
    ordenado_merge = merge_sort(dados_teste, "quantidade_consumida")
    for item in ordenado_merge:
        print(item)

    print("\nOrdenado por Validade (Quick Sort):")
    ordenado_quick = quick_sort(dados_teste, "validade")
    for item in ordenado_quick:
        print(item)
