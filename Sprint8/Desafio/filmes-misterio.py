import sys
import boto3
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
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

# Caminho final com nome do arquivo
dest_path = f"{dest_base_path}/Trusted/Local/Parquet/movies/{ano}/{mes}/{dia}/filmes_misterio"

# Carregar o arquivo CSV do S3 com inferência automática de tipos
df = spark.read.csv(source_path, sep="|", inferSchema=True, header=True)

# Corrigir nome das colunas erradas
df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal").withColumnRenamed("id", "imdb_id")

# Criar a tabela temporária
df.createOrReplaceGlobalTempView("filmesMystery")

# Realizar a consulta e filtro
df = spark.sql("""
    SELECT imdb_id, tituloPrincipal, tituloOriginal, anoLancamento, genero, notaMedia, numeroVotos
    FROM global_temp.filmesMystery
    WHERE genero LIKE '%Mystery%'
""")

# Remover duplicatas
df = df.dropDuplicates()

# Remover linhas com valores nulos
df = df.dropna()

# Garantir que o arquivo seja salvo como um único Parquet
df.repartition(1).write.mode("overwrite").parquet(dest_path)

# INPUT = s3://data-lake-pedroisse/Raw/Local/CSV/Movies/2025/01/03/
# OUTPUT = s3://data-lake-pedroisse/