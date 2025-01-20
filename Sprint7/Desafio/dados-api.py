import requests
import os
import json
import boto3
from datetime import datetime
from dotenv import load_dotenv

def executar_script():
    # Carrega as variáveis de ambiente
    load_dotenv()

    # Chave de acesso (API TMDB)
    api_key = os.getenv('api_key')

    # IDs das coleções (Scream, Friday the 13th, Saw, The Texas Chain Saw Massacre)
    colecoes_ids = [2602, 9735, 656, 111751]

    # Obtém a data atual para o caminho no S3
    data_hoje = datetime.now()
    ano = data_hoje.strftime('%Y')
    mes = data_hoje.strftime('%m')
    dia = data_hoje.strftime('%d')

    # Nome do bucket S3
    nome_bucket = 'data-lake-pedroisse'
    caminho_s3 = f'Raw/TMDB/JSON/{ano}/{mes}/{dia}/terror-slasher.json'

    # Inicializa o cliente S3 (sem credenciais explícitas no Lambda)
    s3_client = boto3.client('s3', region_name="us-east-1")

    # Dicionário para armazenar os dados
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

                    # Busca roteirista(s)
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
                        "director": diretores,
                        "writers": roteiristas,
                        "cast": [ator['name'] for ator in top_20_atores],
                        "characters": [ator['character'] for ator in top_20_atores]
                    })

            dados_colecoes[colecao_id] = {
                "collection_name": dados.get('name'),
                "collection_description": dados.get('overview'),
                "filmes": filmes_detalhados
            }
        
        else:
            print(f"Erro ao buscar dados para a coleção {colecao_id}. Status Code: {resposta.status_code}")

    # Converte para JSON
    json_data = json.dumps(dados_colecoes, ensure_ascii=False, indent=4)

    # Upload direto para S3
    try:
        s3_client.put_object(
            Bucket=nome_bucket,
            Key=caminho_s3,
            Body=json_data,
            ContentType="application/json"
        )

        print(f'Arquivo enviado com sucesso para {caminho_s3} no bucket {nome_bucket}')
        return {"statusCode": 200, "body": "Upload realizado com sucesso"}

    except Exception as e:
        print(f'Erro ao enviar o arquivo para S3: {e}')
        return {"statusCode": 500, "body": f"Erro ao enviar arquivo: {str(e)}"}

def lambda_handler(event, context):
    return executar_script()
