# Abre o arquivo actors.csv e usando ALIAS arquivo para se referir a ele. O with garante que depois da leitura o arquivo será fechado
with open('actors.csv') as arquivo:
    # Crio uma coleção (Dicionário)
    aparicoesFilmes = {}

    # Pula o cabeçalho do arquivo, para que assim só faça análise de dados significativos
    next(arquivo)
    for registro in arquivo:
        # Por conta do ator Robert Downey, Jr o split por vírgula cria um problema, para resolver crio um if que irá verificar se há um aspas duplo
        # que representa o ator
        if '"' in registro:
            separador = registro.strip().split('"')
            restante = separador[2].strip().split(',')
            # Variável filme recebe o filme #1 de cada ator
            filme = restante[4]
        else:
            separador = registro.strip().split(',')
            # Variável filme recebe o filme #1 de cada ator
            filme = separador[4]

        # Se tiver uma chave igual ao conteúdo de filme, ele soma o valor associado a chave em 1
        if filme in aparicoesFilmes.keys():
            aparicoesFilmes[filme] += 1
        else:
        # Caso não, é adicionado como uma chave o conteúdo de filme e é adicionado um valor como 1
            aparicoesFilmes[filme] = 1

# Cria o arquivo etapa-4.txt para escrita
with open('etapa-4.txt', 'w') as saida:
    # Faz a ordem decrescente do dicionário
    aparicoesFilmes = dict(sorted(aparicoesFilmes.items(), key=lambda item: item[1], reverse=True))
    cont = 0

    # Escreve no arquivo o conteúdo do dicionário
    for filme, aparicoes in aparicoesFilmes.items():
        saida.write(f'{cont + 1} - O filme {filme} aparece {aparicoes} de vez(es) no dataset.\n')
