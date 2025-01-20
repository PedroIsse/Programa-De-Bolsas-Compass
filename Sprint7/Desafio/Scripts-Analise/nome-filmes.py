import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Chave da API do TMDb
api_key = os.getenv('api_key')

# Lista de IDs das coleções que você quer buscar
colecoes = {
    "Scream": 2602,
    "Friday the 13th": 9735,
    "Saw": 656,
    "The Texas Chain Saw Massacre": 111751
}

# Nome do arquivo de saída
output_file = "filmes.txt"

# Abre o arquivo para escrita
with open(output_file, "w", encoding="utf-8") as f:
    for nome_colecao, colecao_id in colecoes.items():
        # URL para buscar os filmes da coleção
        url = f"https://api.themoviedb.org/3/collection/{colecao_id}?api_key={api_key}&language=en-US"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            filmes = data.get("parts", [])

            for filme in filmes:
                titulo = filme.get("title", "Título Desconhecido")
                f.write(f'{titulo},')

            f.write("\n")  # Adiciona uma linha em branco entre coleções
        else:
            print(f"Erro ao buscar a coleção {nome_colecao}: {response.status_code}")

print(f"Os títulos dos filmes foram salvos em {output_file} com sucesso!")
