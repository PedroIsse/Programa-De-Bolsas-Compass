# Crio uma função que recebe uma lista e uma função como paramêtros
def my_map(list, f):
    # Usa a lista como paramêtro da função
    nova_lista = f(list)
    # Retorna o resultado da função
    return nova_lista

# Crio uma função chamada de potencia, recebe uma lista como paramêtro   
def potencia(list=[]):
    nova_lista = []
    # Variável nova_lista recebe a potência de cada valor contido na lista recebida como paramêtro
    for i in range(len(list)):
        nova_lista.append(int(list[i]) ** 2)
    # Retorna a nova lista
    return nova_lista
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = my_map(lista, potencia)
print(lista)