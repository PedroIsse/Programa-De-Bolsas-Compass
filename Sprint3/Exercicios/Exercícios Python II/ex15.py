# Crio uma classe chamada Lampada, com 1 atributo e 3 métodos
class Lampada:
    # Atributo ligada, inicialmente, False
    def __init__(self, ligada=False):
        self.ligada = ligada

    # Atributo ligada recebe o valor True, quando a função é chamada
    def liga(self):
        self.ligada = True
    
    # Atributo ligada recebe o valor False, quando a função é chamada
    def desliga(self):
        self.ligada = False
        
    # Atributo ligada retorna seu valor atual, quando a função é chamada
    def esta_ligada(self):
        return self.ligada
        
        
lampada = Lampada()
lampada.liga()
print(f'A lampâda está ligada? {lampada.esta_ligada()}')
lampada.desliga()
print(f'A lâmpada ainda está ligada? {lampada.esta_ligada()}')