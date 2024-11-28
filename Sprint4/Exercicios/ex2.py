def conta_vogais(texto:str)-> int:
    vogais = 'aAeEiIoOuU'
    lista_vogais = list(filter(lambda vogal: vogal in vogais, texto))
    return len(lista_vogais)