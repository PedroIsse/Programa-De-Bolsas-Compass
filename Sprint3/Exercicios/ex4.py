for num in range(1, 101):
    if num >= 2:
        is_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_primo = False
                break
        if is_primo:
            print(num)

