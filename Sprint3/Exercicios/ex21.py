class Passaro:
    def __init__(self, tipo='Passaro'):
        self.tipo = tipo
        
    def voar(self):
        print('Voando...')
        
    def emitir(self, som=''):
        print(f'{self.tipo} emitindo som...')
        print(som)
    
class Pato(Passaro):
    def __init__(self, tipo='Pato'):
        super().__init__(tipo)
    
class Pardal(Passaro):
    def __init__(self, tipo='Pardal'):
        super().__init__(tipo)
        
        
pato = Pato()
print(pato.tipo)
pato.voar()
pato.emitir('Quack Quack')

pardal = Pardal()
print(pardal.tipo)
pardal.voar()
pardal.emitir('Piu Piu')