import random 
numero = 0
lista = []
separacao_numero = ","

while numero < 10000:
    lista.append(str(radom.randint(1, 10000)))
    numero += 1

resultado = separacao_numero.join(lista)

with open ('lista.csv', 'w') as file:
    file.write(resultado)
