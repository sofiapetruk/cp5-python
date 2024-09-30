#recursão - código simples porém o entendimento não é 
# Recursividade - pegar um problema grande / complexa quebrar em problemas menos complexos e depois juntar tudo
# não pode ficar alocando de novo e de novo, exemplo o menu aloca valida e depos que aloca menu e continuação


#Exemplo que não resursão
#Calcular a soma de uma lista de números (sem recursão)

def soma_numeros(lista):
    soma = 0
    for i in lista: #i assume os valores da lista
        soma += i
    return soma



    

#Principal
lista = [1,3,5,7,9]
print(f'Soma: {soma_numeros(lista)}')    

