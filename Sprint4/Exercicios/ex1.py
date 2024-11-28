with open('number.txt', 'r') as arquivo:
    dados = list(map(int, arquivo.readlines()))
    
dados_ordenados = sorted(dados)

pares = list(filter(lambda x: x % 2 == 0, dados_ordenados))

cinco_maiores = pares[-5:][::-1]

print(cinco_maiores)
print(sum(cinco_maiores))
