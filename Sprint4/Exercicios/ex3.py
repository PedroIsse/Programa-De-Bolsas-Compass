from functools import reduce


def calcula_saldo(lancamentos) -> float:
    valor_real = map(lambda valores: valores[0] if valores[1] == 'C' else -valores[0], lancamentos)
    return reduce(lambda lancamento, resultado: lancamento + resultado, valor_real)