# Adiciona a biblioteca functools para ter acesso ao reduce

from functools import reduce

# Cria uma função que calcula o saldo de uma lista de tuplas
def calcula_saldo(lancamentos) -> float:

    # Itera pelos valores da lista e verifica as condições, se for igual a Crédito o valor permanece igual, caso seja Débito
    # o valor será NEGATIVADO
    valor_real = map(lambda valores: valores[0] if valores[1] == 'C' else -valores[0], lancamentos)

    # Usa a função do reduce para iterar a lista retornar a soma REAL dos lançamentos contábeis
    return reduce(lambda lancamento, resultado: lancamento + resultado, valor_real)