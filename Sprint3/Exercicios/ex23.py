class Calculo:
    def soma(self, x=0, y=0):
        self.x = x
        self.y = y
        return x + y
        
    def subtracao(self, x=0, y=0):
        self.x = x
        self.y = y
        return x - y
        
var = Calculo()
x = 4
y = 5

print(f'Somando: {x}+{y} = {var.soma(x, y)}')
print(f'Subtraindo: {x}-{y} = {var.soma(x, y)}')