import random

random_list = random.sample(range(500), 50)

random_list.sort()

mediana = (random_list[24] + random_list[25]) / 2
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')