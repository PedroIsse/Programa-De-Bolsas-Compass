# Abre o arquivo txt e transforma suas linhas em uma lista e armazena na variável dados

with open('number.txt', 'r') as arquivo:
    dados = list(map(int, arquivo.readlines()))
    
# Usa a função sorted para ordenar os dados

dados_ordenados = sorted(dados)

# Filtra na lista de dados, somente, os valores pares

pares = list(filter(lambda x: x % 2 == 0, dados_ordenados))

# Armazena os cinco últimos números (cinco maiores) armazenados na lista "pares"

cinco_maiores = pares[-5:][::-1]

# Imprime os resultados na tela (Cinco maiores números pares e a soma entre eles)

print(cinco_maiores)
print(sum(cinco_maiores))
