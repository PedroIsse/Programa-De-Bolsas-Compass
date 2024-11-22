# Abre o arquivo actors.csv e usando ALIAS arquivo para se referir a ele. O with garante que depois da leitura o arquivo será fechado
with open('actors.csv') as arquivo:
    # Crio duas variáveis para armazenar o valor do nome do autor com o maior número de filmes marcados
    maiorNumFilmes = 0
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
            # Variável recebe o número de filmes que o ator armazenado na variável testeAtor fez
            testeMaiorNumFilmes = int(restante[2].strip()) 
        else:
            separador = registro.strip().split(',')
            # Variável recebe o nome do ator
            testeAtor = separador[0].strip() 
            # Variável recebe o número de filmes que o ator armazenado na variável testeAtor fez
            testeMaiorNumFilmes = int(separador[2].strip()) 

        # Verifica se o número de filmes feitos ator armazenado no testeAtor é maior do que o atual com maior número de filmes
        if testeMaiorNumFilmes > maiorNumFilmes: 
            # Caso sim, é armazeado nas variáveis maiorNumFilmes e nomeAtor as informações
            maiorNumFilmes = testeMaiorNumFilmes
            nomeAtor = testeAtor

# Cria o arquivo etapa-1.txt para escrita
with open('etapa-1.txt', 'w') as saida:
    # Será printado o ator com o maior número de produções
    saida.write(f'Ator com o maior número de filmes: {nomeAtor}, Número de filmes: {maiorNumFilmes}')
