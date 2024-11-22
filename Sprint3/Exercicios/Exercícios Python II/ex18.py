speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
# Transforma em conjunto e garente que não haja valores duplicados no dicionário
aux = set(speed.values())
# Transforma em uma lista e printa os valores
lista = list(aux)

print(lista)