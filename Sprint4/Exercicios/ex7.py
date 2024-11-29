def pares_ate(n:int):
    generator = (valor for valor in range(2, n+1) if valor % 2 == 0)
    return generator