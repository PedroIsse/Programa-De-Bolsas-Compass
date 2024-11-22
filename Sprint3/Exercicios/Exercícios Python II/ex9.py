primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

# Usa a função enumerate para que possa printar todos os valores no formato de iteração
for i, nome in enumerate(primeirosNomes):
    print(f'{i} - {nome} {sobreNomes[i]} está com {idades[i]} anos')
    