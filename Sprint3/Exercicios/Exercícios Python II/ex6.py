a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Transformo as listas em conjuntos, assim retirando as repetições e permitindo métodos como intersection
a = set(a)
b = set(b)

# list_intersection recebe a intersecção dos conjuntos a e b, assim só tendo o que eles tem em comum
list_intersection = list(a.intersection(b))

print(list_intersection)
