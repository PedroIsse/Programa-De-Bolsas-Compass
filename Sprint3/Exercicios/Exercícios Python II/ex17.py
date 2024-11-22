# Crio uma função que divide uma lista em 3 pedaços
def dividir(lista=[]):
    tamanho = len(lista)
    # Descubro o tamanho que cada 'fatia' da lista deve ter
    tamanho_fatia = tamanho // 3
    # A primeira fatia começa do primeiro conteúdo até o tamanho máximo que a fatia deveria ter
    fatia1 = lista[:tamanho_fatia]
    # A segunda fatia começa pelo tamanho máximo da fatia e depois seu dobro, para que assim tenha o mesmo tamanho da anterior e mantenha a sequência
    fatia2 = lista[tamanho_fatia:tamanho_fatia*2]
    # A terceira fatia começa pelo dobro do tamanho máximo até o final da lista
    fatia3 = lista[tamanho_fatia*2:]
    # Retorna o conteúdo de cada fatia
    return fatia1, fatia2, fatia3
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

fatia1, fatia2, fatia3 = dividir(lista)

print(f'{fatia1} {fatia2} {fatia3}')