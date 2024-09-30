def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def menu():
   
    print("\033[35m Escolha o tipo de ordenação: \033[0m")
    print("--- 1 - Bubble Sort---")
    print("---2 - Selection Sort---")
    print("---3 - Insertion Sort---")
    opcao = int(input("Digite o número da opção desejada: "))

    
    if opcao == 1:
        lista_ordenada = bubble_sort(lista)
    elif opcao == 2:
        lista_ordenada = selection_sort(lista)
    elif opcao == 3:
        lista_ordenada = insertion_sort(lista)
    else:
        print("Opção inválida!")
        return print("Lista ordenada:", lista_ordenada)


if __menu__nome__ == "__menu__":
    return menu()