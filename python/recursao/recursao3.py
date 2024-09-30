#Calcular do Fatorial (com recursão)

def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial(n-1)


def fatre_margarete(n):
    if(n == 0 or n==1):
        return 1
    return n * fatre(n-1)    

#Principal
num = int(input("Número: "))
print(f"Fatorial de {num}: {fatorial(num)}")   

print(f"Fatorial: {fatorial(5)}")