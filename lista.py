import random 
numero = 0
lista = []
separacao_numero = ", "

while numero < 350000:
    lista.append(str(random.randint(1, 350000)))
    numero += 1

resultado = separacao_numero.join(lista)

with open ('lista.txt', 'w') as file:
    file.write(resultado)
