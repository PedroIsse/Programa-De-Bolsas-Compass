# Cria uma função que retorna o maior entre as operações fornecidas

def calcular_valor_maximo(operadores,operandos) -> float:

    # A função "zip" junta as listas de operadores e operandos, assim criando um lista de tuplas, podendo formar operações matemáticas
    expressoes = zip(operadores, operandos)

    # A função "eval" irá transformar o operador que está em formato de string, em um operador DE FATO
    # Assim podendo gerar uma operação diferente em cada tupla
    resultados = map(lambda opr: eval(f'{opr[1][0]} {opr[0]} {opr[1][1]}'), expressoes)

    # Retorna o valor máximo (maior valor) da lista "resultados"
    return(max(resultados))