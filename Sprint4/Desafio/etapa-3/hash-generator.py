import hashlib 

def hexdigest(usr_input):
    def encode(usr_input):
        return hashlib.sha1(usr_input.encode())
    return encode(usr_input).hexdigest()


while 1:
    usr_input = input("Digite o texto para gerar o hash SHA-1: ")
    hash_output = hexdigest(usr_input)

    print(f'Gerado o hash SHA-1: {hash_output}')
    