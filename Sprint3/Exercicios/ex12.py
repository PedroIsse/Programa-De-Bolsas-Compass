def my_map(list, f):
    nova_lista = f(list)
    return nova_lista
    
def potencia(list=[]):
    nova_lista = []
    for i in range(len(list)):
        nova_lista.append(int(list[i]) ** 2)
    return nova_lista
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = my_map(lista, potencia)
print(lista)