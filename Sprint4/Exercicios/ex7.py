# Cria uma função que retorna somente os números pares de uma função, utilizando GENERATOR

def pares_ate(n:int):

    # Retorna os números pares incluindo o 2 e o N
    generator = (valor for valor in range(2, n+1) if valor % 2 == 0)

    # Retorna os números pares
    return generator