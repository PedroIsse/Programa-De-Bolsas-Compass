# Abre o arquivo actors.csv e usando ALIAS arquivo para se referir a ele. O with garante que depois da leitura o arquivo será fechado
with open('actors.csv') as arquivo:
    # Crio as variáveis maiorMediaReceita e nomeAtor
    maiorMediaReceita = 0.0
    nomeAtor = ''

    # Pula o cabeçalho do arquivo, para que assim só faça análise de dados significativos
    next(arquivo)
    for registro in arquivo:
        # Por conta do ator Robert Downey, Jr o split por vírgula cria um problema, para resolver crio um if que irá verificar se há um aspas duplo
        # que representa o ator
        if '"' in registro:
            # Separo por aspas duplas, assim que passarem, volto a fazer o split com a vírgula
            separador = registro.strip().split('"')
            # Variável recebe o nome do ator
            testeAtor = separador[1]
            restante = separador[2].split(',')
            # Variável recebe a média de receita de bilheteria do ator armazenado em testeAtor
            testeMaiorMediaReceita = float(restante[3].strip())
        else:
            separador = registro.strip().split(',')
            # Variável recebe o nome do ator
            testeAtor = separador[0].strip()
            # Variável recebe a média de receita de bilheteria do ator armazenado em testeAtor
            testeMaiorMediaReceita = float(separador[3].strip())

        # Verfica se a média de receita de bilheteria do ator armazenado em testeAtor é maior do que a média armazenada em maiorMediaReceita
        if testeMaiorMediaReceita > maiorMediaReceita:
            # Se for maior recebe a média de bilheteria e o nome do ator
            maiorMediaReceita = testeMaiorMediaReceita
            nomeAtor = testeAtor

# Cria o arquivo etapa-3.txt para escrita
with open('etapa-3.txt', 'w') as saida:
    # Escreve no arquivo qual o ator com a maior média de receita de bilheteria e a sua média
    saida.write(f'Ator com o maior média de receita de bilheteria: {nomeAtor}, Média Receita: {maiorMediaReceita}')
