# Crio uma função que recebe um texto com números separados por vírgula
def soma(texto):
    soma = 0
    # Separo por vírgulas e depois faço a soma do conteúdo usando cast(int)
    for i in texto.split(','):
        soma += int(i.strip())
    # Retorno a soma dos valores escritos no texto
    return soma
    
string = soma("1,3,4,6,10,76")
print(string)