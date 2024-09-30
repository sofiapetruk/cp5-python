def selection_sort(lista):
    n = len(lista)  # Obtém o tamanho da lista
    for i in range(n):  # Itera sobre cada elemento
        min_idx = i  # Assume que o primeiro elemento é o menor
        for j in range(i+1, n):  # Compara com os elementos restantes
            if lista[j] < lista[min_idx]:  # Se encontrar um menor
                min_idx = j  # Atualiza o índice do menor
        lista[i], lista[min_idx] = lista[min_idx], lista[i]  # Troca o menor para a posição correta
    return lista  # Retorna a lista ordenada

# Programa Principal
lista = [12, 11, 13, 5, 6, 7]  # Lista original
print(f'Lista original: {lista}')
selection_sort(lista)  # Chama a função de ordenação
print(f'Lista ordenada: {lista}')  # Exibe a lista ordenada
