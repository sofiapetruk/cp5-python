import time
import random 

def dados():
    dado = int(input("Digite quantos números na lista você deseja ordenar: "))
    return dado

def criacao_dado(dado):
    numero = 0
    lista = []
    separacao_numero = ", "

    while numero < dado:  # Aqui `dado` é um número inteiro
        lista.append(str(random.randint(1, dado)))  # Adiciona números aleatórios à lista
        numero += 1

    resultado = separacao_numero.join(lista)  # Junta os números em uma string separada por ", "

    with open('lista.txt', 'w') as file:
        file.write(resultado)  # Grava o resultado no arquivo 'lista.txt'


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
        opcao = int(input("Escolha uma opção de 1 ao 5:"))
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
    # Inicializa uma lista vazia que será preenchida com números inteiros do arquivo
    lista_original = []

    # Abre o arquivo 'lista.txt' em modo de leitura, com codificação UTF-8
    with open('lista.txt', 'r', encoding='utf-8') as file:
        lista = file.read() # Lê todo o conteúdo do arquivo e armazena na variável 'lista' como uma string

    numero_lista = lista.split(",") # Divide a string lida onde há vírgulas, resultando em uma lista de strings

    for i in numero_lista: # Percorre cada item da lista 'numero_lista'
        try:
            lista_original.append(int(i.strip())) # Remove espaços em branco com strip() e tenta converter o item para inteiro
        except ValueError:
            print(f"Valor inválido encontrado: '{i}'")

    print(f'Lista original: {lista_original}') #coloquei aqui se não tinha que colocarm esse print em todas as 4 opreções
        

    while True:
        dado = dados()  
        criacao_dado(dado)

        opcao = menu()
        
        if opcao == 1:
            
            lista_ordenada = lista_original[:]

            tempo = get_time(bubble_sort, lista_ordenada)  # Passar cópia da lista

            print(f'Lista ordenada: {lista_ordenada}') 

            print(f'Tempo de execução do Bubble Sort: {tempo:.3f} segundos')  

        if opcao == 2:
            #print(f'Lista original: {lista}')

            lista_ordenada = lista_original[:]

            tempo = get_time(insertion_sort, lista_ordenada) 

            print(f'Lista ordenada: {lista_original}')  

            print(f'Tempo de execução do Inserting Sort: {tempo:.3f} segundos')   

        if opcao ==3:
            

            lista_ordenada = lista_original[:]

            tempo = get_time(selection_sort, lista_ordenada) 

            print(f'Lista ordenada: {lista_original}')

            print(f'Tempo de execução do Selection Sort: {tempo:.3f} segundos') 


        if opcao == 4:
            # Faz uma cópia da lista original e atribui à variável 'lista_ordenada'
            # O uso de [:] faz uma cópia completa da lista, mantendo a lista original intacta
            lista_ordenada = lista_original[:]

            # Mede o tempo de execução do algoritmo 'bubble_sort' aplicado à lista copiada 'lista_ordenada'
            # O 'get_time' é uma função que retorna o tempo total que o algoritmo leva para ordenar a lista
            # Passamos 'lista_ordenada' (a cópia) para que a lista original não seja modificada
            tempo = get_time(merge_sort, lista_ordenada)

            print(f'Lista ordenada: {lista_original}') # Exibe a lista que foi ordenada após a execução do algoritmo

            print(f'Tempo de execução Merge Sort: {tempo:.3f} segundos')

        if opcao == 5:
            print("Fim do Programa")  
            break  


def get_time(algoritmo, lista):
    inicio = time.time() # Armazena o tempo inicial (antes da execução do algoritmo)
    algoritmo(lista) # Executa o algoritmo passando a lista como argumento
    fim = time.time()  # Armazena o tempo final (após a execução do algoritmo)
    return (fim - inicio) # Retorna a diferença entre o tempo final e o inicial (tempo de execução)



#Principal
main()


