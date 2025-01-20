import requests
import pandas as pd
from IPython.display import display
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

api_key = os.getenv("api_key")

movie_id = "ID do Filme"

url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"

# Fazendo a requisição HTTP
response = requests.get(url)

# Verificando se a resposta foi bem-sucedida
if response.status_code == 200:
    movie_data = response.json()  # Convertendo a resposta para JSON

    # Verificando se o filme pertence a uma coleção (franquia)
    if "belongs_to_collection" in movie_data and movie_data["belongs_to_collection"]:
        collection_id = movie_data["belongs_to_collection"]["id"]
        collection_name = movie_data["belongs_to_collection"]["name"]
        print(f"O filme pertence à coleção: {collection_name} (ID: {collection_id})")
    else:
        print("Este filme não pertence a nenhuma coleção.")
else:
    print(f"Erro na requisição: {response.status_code}")

