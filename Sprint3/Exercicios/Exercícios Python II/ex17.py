def dividir(lista=[]):
    tamanho = len(lista)
    tamanho_fatia = tamanho // 3
    fatia1 = lista[:tamanho_fatia]
    fatia2 = lista[tamanho_fatia:tamanho_fatia*2]
    fatia3 = lista[tamanho_fatia*2:]
    
    return fatia1, fatia2, fatia3
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

fatia1, fatia2, fatia3 = dividir(lista)

print(f'{fatia1} {fatia2} {fatia3}')