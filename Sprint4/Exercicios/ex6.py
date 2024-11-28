def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo.keys())
    
    
    conteudo_ordenado = dict(sorted(conteudo.items(), key=lambda item: item[1], reverse=False))
    
    return [(chave, valor) for chave, valor in conteudo_ordenado.items() if valor > media]