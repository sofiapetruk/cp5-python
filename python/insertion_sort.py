def insertion_sort(lista):
    # Itera a partir do segundo elemento
    for i in range(1, len(lista)):
        chave = lista[i]  # Armazena o elemento atual (chave)
        j = i - 1  # Inicializa j como o índice anterior
        # Move os elementos que são maiores que a chave uma posição para a direita
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]  # Move o elemento para a direita
            j -= 1  # Decrementa j
        lista[j + 1] = chave  # Insere a chave na posição correta
    return lista  # Retorna a lista ordenada

# Programa Principal
lista = [12, 11, 13, 5, 6, 7]  # Lista original
print(f'Lista original: {lista}')
insertion_sort(lista)  # Chama a função de ordenação
print(f'Lista ordenada: {lista}')  # Exibe a lista ordenada
