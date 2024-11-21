with open('actors.csv') as arquivo:
    maiorMediaReceita = 0.0
    nomeAtor = ''

    next(arquivo)

    for registro in arquivo:
        if '"' in registro:
            separador = registro.strip().split('"')
            testeAtor = separador[1]
            restante = separador[2].split(',')
            testeMaiorMediaReceita = float(restante[3].strip())
        else:
            separador = registro.strip().split(',')
            testeAtor = separador[0].strip()
            testeMaiorMediaReceita = float(separador[3].strip())

        if testeMaiorMediaReceita > maiorMediaReceita:
            maiorMediaReceita = testeMaiorMediaReceita
            nomeAtor = testeAtor

with open('etapa-3.txt', 'w') as saida:
    saida.write(f'Ator com o maior média de receita de bilheteria: {nomeAtor}, Média Receita: {maiorMediaReceita}')
