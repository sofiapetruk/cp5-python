"""
Serve para criar a lista de dados no txt e abre o arquivo lista.txt se não estiver criado
"""

import random 
numero = 0
lista = []
separacao_numero = ", "

while numero < 5000:
    lista.append(str(random.randint(1, 5000)))
    numero += 1

resultado = separacao_numero.join(lista)

with open ('lista.txt', 'w') as file:
    file.write(resultado)
