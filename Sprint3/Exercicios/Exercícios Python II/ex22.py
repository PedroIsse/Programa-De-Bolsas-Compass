# Cria um classe Pessoa, com 1 atributo privado chamado nome, 1 público chamado id e duas funções (get, set)
class Pessoa:
    def __init__(self, id=0):
        # Atributo nome (privado) e id (público)
        self.__nome = ''
        self.id = id
    
    # Função que altera o conteúdo do atributo nome
    def set_nome(self, nomeNovo):
        self.__nome = nomeNovo
    
    # Função que retorna o conteúdo do atributo nome
    def get_nome(self):
        return self.__nome
        
    # Uma funcionalidade que permite criar métodos de acesso (getters) e de modificação (setters)
    nome = property(get_nome, set_nome)
    
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)