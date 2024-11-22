# Abre um arquivo de testo e lê seu conteúdo
with open('arquivo_texto.txt', 'r',) as arquivo_texto:
    # Armazena conteúdo na variável dados e depois printa
    dados = arquivo_texto.read()

print(dados, end='')