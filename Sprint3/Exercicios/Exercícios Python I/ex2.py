# Cria uma lista no formato list comprehesion
numeros = [i for i in range(3)] 

for ehImparPar in numeros:
    # Verifico se é par por meio de um cálculo de módulo
    if ehImparPar % 2 == 0: 
        print(f'Par: {ehImparPar}')
    else:
        print(f'Ímpar: {ehImparPar}')