# Cria um função que printa, respectivamente, os paramêtros não nomeados e depois os nomeados
def funcao(*args, **kwargs):
    # Printa os não nomeados
    for arg in args:
        print(arg)
    # Printa os nomeados (Dicionário)
    for chave, valor in kwargs.items():
        print(valor)

funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)