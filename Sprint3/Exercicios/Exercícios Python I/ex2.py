numeros = [i for i in range(3)] # Cria uma lista no formato list comprehesion

for ehImparPar in numeros:
    if ehImparPar % 2 == 0: # Verifico se é par por meio de um cálculo de módulo
        print(f'Par: {ehImparPar}')
    else:
        print(f'Ímpar: {ehImparPar}')