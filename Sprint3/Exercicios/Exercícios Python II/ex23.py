# Cria um classe Calculo, com dois métodos soma e subtracao
class Calculo:
    def soma(self, x=0, y=0):
        # Soma recebe dois parâmetros númericos e retorna sua soma
        self.x = x
        self.y = y
        return x + y
        
    def subtracao(self, x=0, y=0):
        # Subtração recebe dois parâmetros númericos e retorna sua subtração
        self.x = x
        self.y = y
        return x - y
        
var = Calculo()
x = 4
y = 5

print(f'Somando: {x}+{y} = {var.soma(x, y)}')
print(f'Subtraindo: {x}-{y} = {var.soma(x, y)}')