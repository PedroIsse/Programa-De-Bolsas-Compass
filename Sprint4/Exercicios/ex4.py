def calcular_valor_maximo(operadores,operandos) -> float:
    expressoes = zip(operadores, operandos)
    resultados = map(lambda opr: eval(f'{opr[1][0]} {opr[0]} {opr[1][1]}'), expressoes)
    return(max(resultados))