lista_nomes = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in lista_nomes:
    if i[::-1] == i:
        print('A palavra: {0} é um palíndromo'.format(i))
    else:
        print('A palavra: {0} não é um palíndromo'.format(i))