import random

random_list = random.sample(range(500), 50)

# Ordena a lista (Ordem crescente)
random_list.sort()

# Como a lista sempre terá tamanho de 50 (0 a 49) faço a mediana manualmente
mediana = (random_list[24] + random_list[25]) / 2
# Faço o cálculo da média somando os valores da lista dividido pelo tamanho da lista
media = sum(random_list) / len(random_list)
# Encontra o valor mínimo da lista
valor_minimo = min(random_list)
# Encontra o valor máximo da lista
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')