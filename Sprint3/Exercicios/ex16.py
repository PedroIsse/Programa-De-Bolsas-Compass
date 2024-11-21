def soma(texto):
    soma = 0
    for i in texto.split(','):
        soma += int(i.strip())
    return soma
    
string = soma("1,3,4,6,10,76")
print(string)