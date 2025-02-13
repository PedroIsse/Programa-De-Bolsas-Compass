import sys
import boto3
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, monotonically_increasing_id, col, arrays_zip, row_number
from pyspark.sql.window import Window
from pyspark.sql.types import *
from datetime import datetime

# Definir argumentos de entrada para o script
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

# Criar a sessão do Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Caminhos para o S3 (raw e trusted)
source_path = args['S3_INPUT_PATH']
dest_base_path = args['S3_OUTPUT_PATH']

# Obter data atual para estrutura de diretórios

filmes_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/2025/1/29/filmes/"
personagens_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/2025/1/29/personagens/"
atores_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/2025/1/29/atores/"
diretores_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/2025/1/29/diretores/"
roteiristas_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/2025/1/29/roteiristas/"

# Definir schema correto (mantendo elenco como ArrayType)
schema = StructType([
    StructField("id", LongType(), True),
    StructField("imdb_id", StringType(), True),
    StructField("titulo_original", StringType(), True),
    StructField("data_lancamento", StringType(), True),
    StructField("receita", DoubleType(), True),
    StructField("orcamento", DoubleType(), True),
    StructField("diretores", ArrayType(StringType()), True),
    StructField("roteiristas", ArrayType(StringType()), True),
    StructField("elenco", ArrayType(StringType()), True),
    StructField("personagens", ArrayType(StringType()), True),
    StructField("id_colecao", StringType(), True),
    StructField("nome_colecao", StringType(), True),
])

# Ler os dados JSON
dados = spark.read.schema(schema).json(source_path, mode='PERMISSIVE', multiLine=True)

# Função para criar IDs únicos
def create_unique_ids(dataframe, column_name, id_column_name):
    unique_items = dataframe.select(column_name).distinct()
    window_spec = Window.orderBy(column_name)
    unique_items = unique_items.withColumn(id_column_name, row_number().over(window_spec))
    dataframe_with_ids = dataframe.join(unique_items, column_name, "left")
    return dataframe_with_ids

# Explodir e adicionar IDs para atores e personagens juntos
atores_personagens = dados.select(
    "id", 
    "imdb_id",
    "id_colecao",
    explode(arrays_zip(col("elenco"), col("personagens"))).alias("ator_personagem")
)

# Separar atores e personagens
atores_personagens = atores_personagens.select(
    "id",
    "imdb_id",
    "id_colecao",
    col("ator_personagem.elenco").alias("ator"),
    col("ator_personagem.personagens").alias("personagem")
)

# Criar IDs únicos para atores e personagens
atores_personagens = create_unique_ids(atores_personagens, "ator", "id_ator")
atores_personagens = create_unique_ids(atores_personagens, "personagem", "id_personagem")

atores_personagens.write.mode("overwrite").parquet(f"{dest_base_path}/Trusted/TMDB/Parquet/movies/2025/1/29/atores_personagens/")

# Explodir e adicionar IDs para diretores
diretores = dados.select("id", "imdb_id","id_colecao", explode("diretores").alias("diretor"))
diretores = create_unique_ids(diretores, "diretor", "id_diretor")
diretores.dropna().dropDuplicates()
diretores.write.mode("overwrite").parquet(diretores_path)

# Explodir e adicionar IDs para roteiristas
roteiristas = dados.select("id", "imdb_id", "id_colecao", explode("roteiristas").alias("roteirista"))
roteiristas = create_unique_ids(roteiristas, "roteirista", "id_roteirista")
roteiristas.dropna().dropDuplicates()
roteiristas.write.mode("overwrite").parquet(roteiristas_path)

# Remover as colunas 'roteiristas', 'diretores', 'personagens' e 'elenco' do dataframe principal
dados_principal = dados.drop("roteiristas", "diretores", "personagens", "elenco")
dados_principal.dropna().dropDuplicates()
dados_principal.write.mode("overwrite").parquet(filmes_path)