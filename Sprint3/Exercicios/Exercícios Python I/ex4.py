# Loop de 1 até 100
for num in range(1, 101):
    # Qualquer número menor que 2, NÃO PODE ser primo, se maior is_primo é verdadeiro
    if num >= 2:
        is_primo = True
        # Faço o cálculo e verifico condição para saber se o número é primo
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_primo = False
                break
        # Se finalizou com is_primo como verdadeiro, printa o resultado e segue para a próxima iteração
        if is_primo:
            print(num)

