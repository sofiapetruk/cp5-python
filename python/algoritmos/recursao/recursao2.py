#Calculo do Fatorial (sem recursão)

def fatorial_sofia(numero): #refazer
    numero = int(input("Digite um número que você deseja fazer o fatorial: "))
    soma = 1
    for i in range(numero):
        soma *= i 
    return soma, numero

def fatorial_duda(num): 
    lista = []

    for i in range(num):
        i = num
        num -= 1
        lista.append(i)

    fatorial = 1
    for i in lista:
        fatorial *= i

    return fatorial     


def fatorial_margarete(n):
    if n <= 0:
        return
    for i in range(n-1):
        n += n * i
    return n
                 

def fatorial1(n):  #jeito do professor
    fat = 1
    i = 0
    while i <= n:
        fat *= i
        i +=
    return fat        



#Principal

#Jeito da duda e margarete
print(f"Fatorial: {fatorial(5)}")





#Jeito do professor
#num = int(input("Número: ")) 
#print(f"Fatorial de {num}: {fatorial(num)}")


