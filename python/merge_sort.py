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

#Programa Principal
lista = [12, 11, 13, 5, 6, 7]
print(f'Lista original: {lista}')
merge_sort(lista)
print(f'Lista ordenada: {lista}')                         
            