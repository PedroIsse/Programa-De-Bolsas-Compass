with open('actors.csv') as arquivo:
    atoresOrdenadosTotalGross = {}
    nome = ''
    totalGross = 0.0

    next(arquivo)
    for registro in arquivo:
        if '"' in registro:
            separador = registro.strip().split('"')
            nome = separador[1]
            restante = separador[2].strip().split(',')
            totalGross = float(restante[1])
            atoresOrdenadosTotalGross[nome] = totalGross
        else:
            separador = registro.strip().split(',')
            nome = separador[0]
            totalGross = float(separador[1])
            atoresOrdenadosTotalGross[nome] = totalGross

with open('etapa-5.txt', 'w') as saida:
    atoresOrdenadosTotalGross = dict(sorted(atoresOrdenadosTotalGross.items(), key=lambda item: item[1], reverse=True))
    for nome, totalGrossOrdenado in atoresOrdenadosTotalGross.items():
        saida.write(f'{nome} - {totalGrossOrdenado:.2f}\n')
