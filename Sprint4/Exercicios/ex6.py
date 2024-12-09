# Cria uma função que recebe um dicionário e retorna os Valores que estão acima da média
def maiores_que_media(conteudo:dict)->list:

    # Faz a cálculo da média pela soma dos Valores dividido pelo número de Chaves
    media = sum(conteudo.values()) / len(conteudo.keys())
    
    # O conteúdo de "conteudo" será ordenado em ordem crescente, baseado nos seus Valores, e assim, serão armazenados em um dicionário
    conteudo_ordenado = dict(sorted(conteudo.items(), key=lambda item: item[1], reverse=False))
    
    # Retorna as CHAVES e VALORES (em lista), daqueles que no generator tiverem seu Valor maior que a média
    return list((chave, valor) for chave, valor in conteudo_ordenado.items() if valor > media)