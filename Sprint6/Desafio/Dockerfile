FROM python:3.11.4-slim

# Define o diretório de trabalho no container
WORKDIR /desafio-sprint06

# Instala boto3, botocore e python-dotenv
RUN pip install --no-cache-dir boto3 botocore python-dotenv

# Copia o script e o arquivo .env para o diretório de trabalho no container
COPY upload-arquivos.py .
COPY .env .
COPY movies.csv .
COPY series.csv .
# Comando para executar o script
CMD ["python", "upload-arquivos.py"]
