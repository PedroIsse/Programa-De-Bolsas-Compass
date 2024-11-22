# Cria uma classe Aviao, com 4 atributos
class Aviao:
    # Os atributos são modelo, velocidade_maxima, capacidade e cor, que inicialmente recebe o valor 'azul'
    def __init__(self, modelo, velocidade_maxima, capacidade, cor='azul'):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = cor
        self.capacidade = capacidade

aviao1 = Aviao('BOIENG456', 1500, capacidade=400)
aviao2 = Aviao('Embraer', 863, capacidade=14)
aviao3 = Aviao('Antonov An-2', 258, capacidade=12)

# Crio uma lista que armazena os objetos com seus atributos modificados
lista = [aviao1, aviao2, aviao3]

for aviao in lista:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}')