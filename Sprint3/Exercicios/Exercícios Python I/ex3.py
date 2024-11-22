# Cria um lista que recebe, somente, os números pares entre 0 e 20
lista = [i for i in range(0, 21) if i % 2 == 0]

for ehPar in lista:
    print(ehPar)