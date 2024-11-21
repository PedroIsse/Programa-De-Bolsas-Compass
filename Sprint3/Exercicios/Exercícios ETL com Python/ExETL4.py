with open('actors.csv') as arquivo:
    aparicoesFilmes = {}

    next(arquivo)
    for registro in arquivo:
        if '"' in registro:
            separador = registro.strip().split('"')
            restante = separador[2].strip().split(',')
            filme = restante[4]
        else:
            separador = registro.strip().split(',')
            filme = separador[4]

        if filme in aparicoesFilmes.keys():
            aparicoesFilmes[filme] += 1
        else:
            aparicoesFilmes[filme] = 1



with open('etapa-4.txt', 'w') as saida:
    aparicoesFilmes = dict(sorted(aparicoesFilmes.items(), key=lambda item: item[1], reverse=True))
    cont = 0

    for filme, aparicoes in aparicoesFilmes.items():
        saida.write(f'{cont + 1} - O filme {filme} aparece {aparicoes} de vez(es) no dataset.\n')
