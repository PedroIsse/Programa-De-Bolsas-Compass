import requests
import pandas as pd
from IPython.display import display
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

api_key = os.getenv("api_key")

# Nome do filme para buscar
movie_name = "Nome do Filme"

# URL para pesquisar o filme pelo nome
search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}&language=pt-BR"

response = requests.get(search_url)
if response.status_code == 200:
    results = response.json().get("results", [])
    if results:
        movie_id = results[0]["id"]
        print(f"Filme encontrado: {results[0]["title"]} (ID: {movie_id})")
    else:
        print("Nenhum filme encontrado.")
else:
    print(f"Erro na requisição: {response.status_code}")
