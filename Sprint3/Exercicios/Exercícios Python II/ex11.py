# Importa o módulo json
import json

# Abre o arquivo person.json e lê ele, ALIAS para arquivo
with open('person.json', 'r') as arquivo:
    # Variavel dados recebe o conteúdo lido no arquivo json
    dados = json.load(arquivo)

# Printa o conteúdo do arquivo
print(dados)