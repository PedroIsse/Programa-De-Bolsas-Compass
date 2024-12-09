# Cria uma função que retorna média de uma lista, com duas casas decimais de precisão
def get_media(lista:list) -> float:
    return round(sum(lista) / len(lista), 2)

# Inicializa as listas
nomes_estudantes = []
tres_maiores_notas = []
medias = []

# Abre o arquivo "estudantes.csv" como leitura
with open('estudantes.csv', 'r') as arquivo:
    
    # Itero por cada linha do arquivo
    for linhas in arquivo:
        # Separa como colunas, seperadas por vírgula
        separador = linhas.split(',')

        # Adiciona o nome de um estudante a cada iteração
        nomes_estudantes.append(separador[0])

        # Recebe uma lista com TODAS as notas do estudante da iteração
        notas_estudante = list(map(int, separador[1:]))

        # Faz a ordenação descrescente das notas do estudante da iteração
        tres_maiores_notas.append(sorted(notas_estudante, reverse=True)[:3])

        # Adiciona a média do estudante, a uma lista com todas as médias dos alunos
        medias.append(get_media(tres_maiores_notas[-1]))
        
# Zipa todas as listas juntas, e depois transformo em uma grande lista
resultado = list(zip(nomes_estudantes, tres_maiores_notas, medias))

# Ordena a lista "resultado" por ordem alfabética
resultado.sort(key=lambda x: x[0])

# Imprime o resultado na tela
for alunos in resultado:
    print(f'Nome: {alunos[0]} Notas: {alunos[1]} Média: {alunos[2]}')