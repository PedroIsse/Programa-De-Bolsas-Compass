# Cria uma função que conta o número de vezes que uma vogal aparece em uma string

def conta_vogais(texto:str)-> int:

    # Define vogais com letra maíuscula e mínusculas
    vogais = 'aAeEiIoOuU'

    # Preenche uma lista a qual só armazenará as vogais que compõe a string recebida
    lista_vogais = list(filter(lambda vogal: vogal in vogais, texto))

    # Retorna o tamanho da lista, ou seja, todas as vogais da string
    return len(lista_vogais)