with open('actors.csv') as arquivo:
    media = 0.0
    contLinhas = 0

    next(arquivo)
    for registro in arquivo:
        if '"' in registro:
            separador = registro.strip().split('"')
            restante = separador[2].split(',')
            media += float(restante[5])
        else:
            separador = registro.strip().split(',')
            media += float(separador[5])

        contLinhas += 1

with open('etapa-2.txt', 'w') as saida:
    saida.write(f'A média de receita de bilheteria dos principais filmes dos atores é de: '
                f'{media / contLinhas:.2f} milhões de dólares')
