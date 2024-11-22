a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

ehImpar = []

for i in a:
    # Se o conteúdo da lista iterado divido por 2 tiver resto como 0, o número é par
    if i % 2 != 0:
        ehImpar.append(i)
        
print(ehImpar)