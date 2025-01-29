import sys
import boto3
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.types import *
from pyspark.sql.functions import monotonically_increasing_id
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
now = datetime.now()
ano, mes, dia = now.year, now.month, now.day

filmes_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/{ano}/{mes}/{dia}/filmes/"
personagens_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/{ano}/{mes}/{dia}/personagens/"
atores_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/{ano}/{mes}/{dia}/atores/"
diretores_path =  f"{dest_base_path}/Trusted/TMDB/Parquet/movies/{ano}/{mes}/{dia}/diretores/"
roteiristas_path = f"{dest_base_path}/Trusted/TMDB/Parquet/movies/{ano}/{mes}/{dia}/roteiristas/"

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

dados = spark.read.schema(schema).json(source_path, mode='PERMISSIVE', multiLine=True)

# Explodir a coluna "elenco" para transformar cada ator em uma linha separada e adicionar um ID único
atores = dados.select(
    "id", "imdb_id", explode("elenco").alias("ator")
).withColumn("id_ator", monotonically_increasing_id() + 1)

atores.dropna().dropDuplicates()

atores.write.mode("overwrite").parquet(atores_path)

personagens = dados.select(
    "id", "imdb_id", explode("personagens").alias("personagem")
).withColumn("id_personagem", monotonically_increasing_id() + 1)

personagens.dropna().dropDuplicates()

personagens.write.mode("overwrite").parquet(personagens_path)

diretores = dados.select(
    "id", "imdb_id", explode("diretores").alias("diretor")
).withColumn("id_diretor", monotonically_increasing_id() + 1)

diretores.dropna().dropDuplicates()

diretores.write.mode("overwrite").parquet(diretores_path)

roteiristas = dados.select(
    "id", "imdb_id", explode("roteiristas").alias("roteiristas")
).withColumn("id_roteirista", monotonically_increasing_id() + 1)

roteiristas.dropna().dropDuplicates()

roteiristas.write.mode("overwrite").parquet(roteiristas_path)

# Remover as colunas 'roteiristas', 'diretores', 'personagens' e 'elenco' do dataframe principal
dados_principal = dados.drop("roteiristas", "diretores", "personagens", "elenco")

dados_principal.dropna().dropDuplicates()

dados_principal.write.mode("overwrite").parquet(filmes_path)
