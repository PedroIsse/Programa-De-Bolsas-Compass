# Abre o arquivo actors.csv e usando ALIAS arquivo para se referir a ele. O with garante que depois da leitura o arquivo será fechado
with open('actors.csv') as arquivo:
    # Crio uma coleção (Dicionário) atoresOrdenadosTotalGross, nome e totalGross 
    atoresOrdenadosTotalGross = {}
    nome = ''
    totalGross = 0.0

    # Pula o cabeçalho do arquivo, para que assim só faça análise de dados significativos
    next(arquivo)
    for registro in arquivo:
        # Por conta do ator Robert Downey, Jr o split por vírgula cria um problema, para resolver crio um if que irá verificar se há um aspas duplo
        # que representa o ator
        if '"' in registro:
            separador = registro.strip().split('"')
            # nome recebe o nome do ator
            nome = separador[1] 
            restante = separador[2].strip().split(',')
            # totalGross recebe a receita bruta de bilheteria
            totalGross = float(restante[1]) 
            # Coloca o nome do ator como chave do dicionário e o valor como totalGross
            atoresOrdenadosTotalGross[nome] = totalGross
        else:
            separador = registro.strip().split(',')
            # nome recebe o nome do ator
            nome = separador[0]
            # totalGross recebe a receita bruta de bilheteria
            totalGross = float(separador[1])
            # Coloca o nome do ator como chave do dicionário e o valor como totalGross
            atoresOrdenadosTotalGross[nome] = totalGross

# Cria o arquivo etapa-5.txt para escrita
with open('etapa-5.txt', 'w') as saida:
    # Faz a ordem decrescente do dicionário
    atoresOrdenadosTotalGross = dict(sorted(atoresOrdenadosTotalGross.items(), key=lambda item: item[1], reverse=True))
    # Escreve o nome do autor e sua receita bruta de bilheteria
    for nome, totalGrossOrdenado in atoresOrdenadosTotalGross.items():
        saida.write(f'{nome} - {totalGrossOrdenado:.2f}\n')
