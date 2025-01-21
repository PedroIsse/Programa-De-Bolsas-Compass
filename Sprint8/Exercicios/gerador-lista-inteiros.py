import random

num_int = []

# Gerar 250 números aleatórios entre 0 e 250
for _ in range(250):
    num_int.append(random.randint(0, 250))

# Inverter a lista
num_int.reverse()

# Exibir a lista invertida
print(num_int)
