import boto3
from botocore.exceptions import ClientError

# Nome do perfil configurado com o AWS SSO
perfil_sso = 'pedroisse'

nome_bucket = 'desafio-sprint05-pedroisse'
dataset = 'veiculos-habilitados-12-2024.csv'
caminho_dataset = './veiculos-habilitados-12-2024.csv'

# Inicializa a sessão com o perfil SSO
sessao = boto3.Session(profile_name=perfil_sso)

# Inicializa o cliente S3 usando a sessão SSO
cliente_s3 = sessao.client(
    "s3",
    region_name="us-east-1"
)

# Criando o bucket
try:
    resposta = cliente_s3.create_bucket(
        Bucket=nome_bucket
    )

    # Confirmação de que o Bucket foi criado com sucesso
    print(f"Bucket {nome_bucket} criado com sucesso!")
except ClientError as e:
    
    # Caso não tenha dado certo, ele devolve o erro 
    print(f"Erro ao criar o bucket: {e}")

# Fazendo Upload no Dataset original
try:
    cliente_s3.upload_file(caminho_dataset, nome_bucket, dataset)

    # Confirmação de que o dataset foi enviado
    print(f'Arquivo {dataset} enviado com sucesso ao bucket {nome_bucket}')
except Exception as e:

    # Caso não tenha dado certo, ele devolve o erro
    print(f'Erro ao enviar o arquivo: {e}')