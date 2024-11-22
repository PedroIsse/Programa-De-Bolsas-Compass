lista_nomes = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in lista_nomes:
    # Verifica se cada conteúdo da lista é igual o conteúdo dela "ao contrário"
    if i[::-1] == i:
        # Se sim avisa que é um palíndromo
        print('A palavra: {0} é um palíndromo'.format(i))
    else:
        # Se não avisa que não é um palíndromo
        print('A palavra: {0} não é um palíndromo'.format(i))