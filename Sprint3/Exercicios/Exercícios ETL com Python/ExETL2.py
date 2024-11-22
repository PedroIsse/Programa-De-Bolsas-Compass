# Abre o arquivo actors.csv e usando ALIAS arquivo para se referir a ele. O with garante que depois da leitura o arquivo será fechado
with open('actors.csv') as arquivo:
    # Crio as variáveis media e contLinhas
    media = 0.0
    contLinhas = 0

    # Pula o cabeçalho do arquivo, para que assim só faça análise de dados significativos
    next(arquivo)
    for registro in arquivo:
        # Por conta do ator Robert Downey, Jr o split por vírgula cria um problema, para resolver crio um if que irá verificar se há um aspas duplo
        # que representa o ator
        if '"' in registro:
            # Separo por aspas duplas, assim que passarem, volto a fazer o split com a vírgula
            separador = registro.strip().split('"')
            restante = separador[2].split(',')
            # media recebe todas as iterações do conteúdo armazenado no sexto campo depois da vírgula (Gross)
            media += float(restante[5]) 
        else:
            separador = registro.strip().split(',')
            # media recebe todas as iterações do conteúdo armazenado no sexto campo depois da vírgula (Gross)
            media += float(separador[5])

        contLinhas += 1 # Conta quantas linhas o arquivo tem

# Cria o arquivo etapa-2.txt para escrita
with open('etapa-2.txt', 'w') as saida:
    # Escrevo qual a média de receita de bilheteria dos principais filmes dos atores fazendo uma média simples
    saida.write(f'A média de receita de bilheteria dos principais filmes dos atores é de: '
                f'{media / contLinhas:.2f} milhões de dólares')
