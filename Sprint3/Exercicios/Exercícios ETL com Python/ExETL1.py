with open('actors.csv') as arquivo:
    maiorNumFilmes = 0
    nomeAtor = ''

    next(arquivo)

    for registro in arquivo:
        if '"' in registro:
            separador = registro.strip().split('"')
            testeAtor = separador[1]
            restante = separador[2].split(',')
            testeMaiorNumFilmes = int(restante[2].strip())
        else:
            separador = registro.strip().split(',')
            testeAtor = separador[0].strip()
            testeMaiorNumFilmes = int(separador[2].strip())

        if testeMaiorNumFilmes > maiorNumFilmes:
            maiorNumFilmes = testeMaiorNumFilmes
            nomeAtor = testeAtor

with open('etapa-1.txt', 'w') as saida:
    saida.write(f'Ator com o maior número de filmes: {nomeAtor}, Número de filmes: {maiorNumFilmes}')
