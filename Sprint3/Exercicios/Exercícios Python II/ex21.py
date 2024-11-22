# Cria uma classe Passaro com 1 atributo e 2 métodos
class Passaro:
    # Atributo "tipo", que recebe o tipo de pássaro
    def __init__(self, tipo='Passaro'):
        self.tipo = tipo
   
    def voar(self):
        print('Voando...')
    
    # O método recebe um paramêtro com o som que o animal faz
    def emitir(self, som=''):
        # Printa o animal que faz o som e o som que ele faz depois
        print(f'{self.tipo} emitindo som...')
        print(som)

# Herança de Passaro -> Pato
class Pato(Passaro):
    def __init__(self, tipo='Pato'):
        super().__init__(tipo)

# Herança de Passaro -> Pardal   
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