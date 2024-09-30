import random
import time

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Cria uma lista de 5000 elementos aleatórios
tamanho = 5000
lista = [random.randint(0, 10000) for _ in range(tamanho)]

# Mede o tempo de execução
def get_time(arg):
    inicio=time.time()
    time.sleep(arg)
    fim=time.time()
    return fim_inicio


#principal
dif = get.time(1) #teste
print(f'Dif: {dif:.2f}')

# Exibe o tempo gasto
print(f"Tempo de execução: {fim - inicio:.6f} segundos")

