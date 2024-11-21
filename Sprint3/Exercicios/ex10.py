def lista_nova(lista=[]):
    return list(set(lista))

listaAtual = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
listaAtual = lista_nova(listaAtual)
print(listaAtual)