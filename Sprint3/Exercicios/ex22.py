class Pessoa:
    def __init__(self, id=0):
        self.__nome = ''
        self.id = id
    
    def set_nome(self, nomeNovo):
        self.__nome = nomeNovo

    def get_nome(self):
        return self.__nome
        
    nome = property(get_nome, set_nome)
    
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)