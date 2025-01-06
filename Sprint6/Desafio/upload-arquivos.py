import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se as variáveis de ambiente foram configuradas corretamente
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.getenv('AWS_SESSION_TOKEN')

# Nome do bucket e informações do dataset
nome_bucket = 'data-lake-pedroisse'
caminho_movies = './movies.csv'
caminho_series = './series.csv'

# Obtém a data atual
data_hoje = datetime.now()
ano = data_hoje.strftime('%Y')
mes = data_hoje.strftime('%m')
dia = data_hoje.strftime('%d')

dataset_movies = f'Raw/Local/CSV/Movies/{ano}/{mes}/{dia}/movies.csv'
dataset_series = f'Raw/Local/CSV/Series/{ano}/{mes}/{dia}/series.csv'

# Inicializa a sessão com o perfil SSO
sessao = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Inicializa o cliente S3 usando a sessão SSO
cliente_s3 = sessao.client(
    "s3",
    region_name="us-east-1"
)

# Fazendo Upload no Dataset original
try:
    cliente_s3.upload_file(caminho_movies, nome_bucket, dataset_movies)

    # Confirmação de que o dataset foi enviado
    print(f'Arquivo {dataset_movies} enviado com sucesso ao bucket {nome_bucket}')

    cliente_s3.upload_file(caminho_series, nome_bucket, dataset_series)

    # Confirmação de que o dataset foi enviado
    print(f'Arquivo {dataset_series} enviado com sucesso ao bucket {nome_bucket}')

except Exception as e:
    # Caso não tenha dado certo, ele devolve o erro
    print(f'Erro ao enviar o arquivo: {e}')
