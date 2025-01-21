import names
import random

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorio = 10000000

# Gerando 3000 nomes únicos
aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f'Gerando {qtd_nomes_aleatorio} nomes aleatórios')

# Gerando 10 milhões de nomes aleatórios
dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorio)]

# Escrevendo os nomes corretamente no arquivo
with open("nomes_aleatorios.txt", "w", encoding="utf-8") as saida:
    for nome in dados:
        saida.write(f'{nome}\n')

print("Arquivo gerado com sucesso!")
