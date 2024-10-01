#Como fazer a soma sem laço de repetição
#Fazer uma soma sem fazer laço você deve usar a recursão
#Usar quando tiver mais de 10 milhoões, não tenhuma função alocadada nela

#Calcular a soma de uma lista de números (com recursão)

def soma_numeros(lista):
    if len(lista) == 1: #primeiro devo fazer o caso base // se o tamanho da lista for igual a 1 quero que ele pare
        return lista[0] #posição do número 1
    else:
        return lista[0] + soma_numeros(lista[1:])  #os dois pontos serve para pegar o número 1 mais os outros ----- guarda o indíce zero e depois pega a lista - 1 elemento ver no tutor python isso 


#Principal
lista = [1,3,5,7,9]
print(f"Soma {soma_numeros(lista)}")         