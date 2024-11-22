# Cria um classe Ordenadora, com 1 atributo e dois métodos
class Ordenadora:
    # Atributo que recebe uma lista
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    # Retorna o atributo listaBaguncada Ordenada (Ordem crescente)
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    # Retorna o atributo listaBaguncada Ordenada (Ordem decrescente)  
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse = True)

crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())