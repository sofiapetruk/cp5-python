def bubble_sort(lista):
    n = len(lista)  # Obtém o tamanho da lista
    for i in range(n):  # Itera sobre cada elemento da lista
        for j in range(0, n-i-1):  # Compara elementos adjacentes
            if lista[j] > lista[j+1]:  # Se o elemento atual é maior que o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Troca os elementos
    return lista  # Retorna a lista ordenada

# Programa Principal
lista = [12, 11, 13, 5, 6, 7]  # Lista original
print(f'Lista original: {lista}')
bubble_sort(lista)  # Chama a função de ordenação
print(f'Lista ordenada: {lista}')  # Exibe a lista ordenada
