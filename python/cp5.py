import time


def menu():
    print("""
    Escolha uma opção:
    (1) - Bubble Sort
    (2) - Insertion Sort
    (3) - Selection Sort
    (4) - Merge Sort
    (5) - Sair do Programa
    """)
    try:
        opcao = int(input("Escolha uma opção de 1 ao 4:"))
        if opcao < 1 or opcao > 5:
            print('Opção inválida. Escolha um número do MENU')
        else:
            return opcao
        
    except ValueError:
        print('Entrada inválida (somente números) você pode digitar. Por favor, digite um número entre 1 a 9.')    
    except  Exception as e:
        print(f'Ocorreu um erro: {e}')
    


def bubble_sort(lista):
    n = len(lista)  # Obtém o tamanho da lista
    for i in range(n):  # Itera sobre cada elemento da lista
        for j in range(0, n-i-1):  # Compara elementos adjacentes
            if lista[j] > lista[j+1]:  # Se o elemento atual é maior que o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Troca os elementos
    return lista  # Retorna a lista ordenada


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

def selection_sort(lista):
    n = len(lista)  # Obtém o tamanho da lista
    for i in range(n):  # Itera sobre cada elemento
        min_idx = i  # Assume que o primeiro elemento é o menor
        for j in range(i+1, n):  # Compara com os elementos restantes
            if lista[j] < lista[min_idx]:  # Se encontrar um menor
                min_idx = j  # Atualiza o índice do menor
        lista[i], lista[min_idx] = lista[min_idx], lista[i]  # Troca o menor para a posição correta
    return lista  # Retorna a lista ordenada    

def merge_sort(lista):
    if len(lista) > 1:

        #encontrar o meio da lista
        meio = len(lista) // 2 #divisão inteira

        #dividindo a lista em duas sub-listas (L - R)
        #fatiamento de listas
        L = lista[:meio]
        R = lista[meio:]

        #chamada recursiva
        merge_sort(L)

        merge_sort(R)

        #variáveis de controle
        # i - fará o controle da lista L
        # j - fará o controle da lista R
        #k - fará o controle da lista antes da recursão

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i+=1
            else:
                lista[k] = R[j]
                j+=1
            k+=1


        #verificação dos elementos da lista L
        while i < len(L):
            i+=1
            k+=1

        #verificação dos elementos da lista R
        while j < len(R):
            lista[k] = R[j]
            j+=1
            k+=1  

def main():
    lista_original = []
    with open('lista.txt', 'r', encoding='utf-8') as file:
        lista = file.read()

    numero_lista = lista.split(",")

    for i in numero_lista:
        try:
            lista_original.append(int(i.strip()))
        except ValueError:
            print(f"Valor inválido encontrado: '{i}'")

    print(f'Lista original: {lista_original}') #coloquei aqui se não tinha que colocarm esse print em todas as 4 opreções
        

    while True:
        opcao = menu()
        
        if opcao == 1:
            
            tempo = get_time(bubble_sort, lista_original[:])  # Passar cópia da lista

            print(f'Lista ordenada: {lista_original}') 

            print(f'Tempo de execução: {tempo:.2f} segundos')  

        if opcao == 2:
            #print(f'Lista original: {lista}')

            tempo = get_time(insertion_sort, lista_original[:]) 

            print(f'Lista ordenada: {lista_original}')  

            print(f'Tempo de execução: {tempo:.2f} segundos')   

        if opcao ==3:
            #print(f'Lista original: {lista}')

            tempo = get_time(selection_sort, lista_original[:]) 

            print(f'Lista ordenada: {lista_original}')

            print(f'Tempo de execução: {tempo:.2f} segundos') 


        if opcao == 4:
            #print(f'Lista original: {lista}')

            tempo = get_time(merge_sort, lista_original[:])

            print(f'Lista ordenada: {lista_original}')

            print(f'Tempo de execução: {tempo:.2f} segundos')

        if opcao == 5:
            print("Fim do Programa")  
            break  


def get_time(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    return (fim - inicio)



#Principal
main()


