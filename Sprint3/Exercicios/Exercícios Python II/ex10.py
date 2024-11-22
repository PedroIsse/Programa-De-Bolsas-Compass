# Função que recebe uma lista, transforma em um conjunto para retirar valores duplicados, depois transforma em lista novamente
def lista_nova(lista=[]):
    return list(set(lista))

listaAtual = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
# Chama função com listaAtual como paramêtro
listaAtual = lista_nova(listaAtual)
print(listaAtual)