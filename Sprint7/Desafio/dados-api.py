import requests
import os
import json
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Chave de acesso
api_key = os.getenv('api_key')

# IDs das coleções (Scream, Friday the 13th, Saw, The Texas Chain Saw Massacre)
colecoes_ids = [2602, 9735, 656, 111751]

dados_colecoes = {}

for colecao_id in colecoes_ids:
    url = f"https://api.themoviedb.org/3/collection/{colecao_id}?api_key={api_key}&language=pt-BR"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        filmes_detalhados = []

        for filme in dados.get('parts', []):
            filme_id = filme['id']
            
            # Busca detalhes do filme
            url_filme = f"https://api.themoviedb.org/3/movie/{filme_id}?api_key={api_key}&language=pt-BR"
            resposta_filme = requests.get(url_filme)
            
            # Busca créditos do filme (elenco e equipe técnica)
            url_creditos = f"https://api.themoviedb.org/3/movie/{filme_id}/credits?api_key={api_key}&language=pt-BR"
            resposta_creditos = requests.get(url_creditos)

            if resposta_filme.status_code == 200 and resposta_creditos.status_code == 200:
                detalhes_filme = resposta_filme.json()
                creditos = resposta_creditos.json()
                
                top_20_atores = sorted(creditos.get('cast', []), key=lambda x: x['order'])[:20]

                # Busca diretor(es)
                diretores = [pessoa['name'] for pessoa in creditos.get('crew', []) if pessoa['job'] == 'Director']

                # Busca roteirista(s) (Screenplay, Writer, Story)
                roteiristas = [
                    pessoa['name'] for pessoa in creditos.get('crew', [])
                    if pessoa['job'] in ['Writer', 'Screenplay', 'Story']
                ]

                filmes_detalhados.append({
                    "id": detalhes_filme.get('id'),
                    "imdb_id": detalhes_filme.get('imdb_id'),
                    "title": detalhes_filme.get('title'),
                    "original_title": detalhes_filme.get('original_title'),
                    "release_date": detalhes_filme.get('release_date'),
                    "revenue": detalhes_filme.get('revenue'),
                    "budget": detalhes_filme.get('budget'),
                    "vote_average": detalhes_filme.get('vote_average'),
                    "vote_count": detalhes_filme.get('vote_count'),
                    "director": diretores,  # Lista de diretores
                    "writers": roteiristas,  # Lista de roteiristas
                    "cast": [ator['name'] for ator in top_20_atores],  # Nomes dos 20 primeiros atores
                    "characters": [ator['character'] for ator in top_20_atores]  # Personagens interpretados
                })

        dados_colecoes[colecao_id] = {
            "collection_name": dados.get('name'),
            "collection_description": dados.get('overview'),
            "filmes": filmes_detalhados
        }
    
    else:
        print(f"Erro ao buscar dados para a coleção {colecao_id}. Status Code: {resposta.status_code}")

# Salva os dados no arquivo 'dados_colecoes.json'
with open('dados_colecoes.json', 'w', encoding='utf-8') as f:
    json.dump(dados_colecoes, f, ensure_ascii=False, indent=4)

print("Dados das coleções salvos com sucesso!")
