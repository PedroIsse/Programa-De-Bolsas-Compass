import sys
import boto3
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, dayofmonth, monotonically_increasing_id, expr, row_number
from datetime import datetime
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.window import Window

# Função para criar IDs únicos
def create_unique_ids(dataframe, column_name, id_column_name):
    unique_items = dataframe.select(column_name).distinct()
    window_spec = Window.orderBy(column_name)  # Garante que os IDs sejam ordenados
    unique_items = unique_items.withColumn(id_column_name, row_number().over(window_spec))
    dataframe_with_ids = dataframe.join(unique_items, column_name, "left")
    return dataframe_with_ids


# Definir argumentos de entrada para o script
args = getResolvedOptions(sys.argv, 
['JOB_NAME', 'S3_FILMES_TMDB', 'S3_FILMES_TERROR', 'S3_DIRETORES', 'S3_ROTEIRISTAS', 'S3_ATORES_PERSONAGENS','S3_OUTPUT_PATH']
)

# Criar a sessão do Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# INPUT dos Dados
filmes_tmdb_path = args['S3_FILMES_TMDB']  # s3://data-lake-pedroisse/Trusted/TMDB/Parquet/movies/2025/1/29/filmes/
filmes_terror_path = args['S3_FILMES_TERROR']  # s3://data-lake-pedroisse/Trusted/Local/Parquet/movies/2025/1/28/filmes_terror/
s3_diretores = args['S3_DIRETORES'] # s3://data-lake-pedroisse/Trusted/TMDB/Parquet/movies/2025/1/29/diretores/
s3_roteiristas = args['S3_ROTEIRISTAS'] # s3://data-lake-pedroisse/Trusted/TMDB/Parquet/movies/2025/1/29/roteiristas/
s3_atores_personagens = args['S3_ATORES_PERSONAGENS'] # s3://data-lake-pedroisse/Trusted/TMDB/Parquet/movies/2025/1/29/atores_personagens/
dest_base_path = args['S3_OUTPUT_PATH'] # s3://data-lake-pedroisse/

# Caminho Final (Criando Tabelas)
atores_path = f"{dest_base_path}/Refined/DimAtores/Dim-Atores/"
personagens_path = f"{dest_base_path}/Refined/DimPersonagens/Dim-Personagens/"
diretores_path = f"{dest_base_path}/Refined/DimDiretores/Dim-Diretores/"
roteiristas_path = f"{dest_base_path}/Refined/DimRoteiristas/Dim-Roteiristas/"
filmes_path = f"{dest_base_path}/Refined/DimFilmes/Dim-Filmes-Slasher/"
colecao_path = f"{dest_base_path}/Refined/DimColecoes/Dim-Colecoes/"
datas_path = f"{dest_base_path}/Refined/DimDatas/Dim-Datas/"
fato_path = f"{dest_base_path}/Refined/FatoFilmes/Fato-Filmes-Slasher/"

# Lista de ID de coleções que queremos filtrar
colecoes_ids = [2602, 9735, 656, 111751]

# Ler a tabela atores_personagens
atores_personagens = spark.read.parquet(s3_atores_personagens)

# Filtrar atores e personagens por id_colecao
atores_personagens = atores_personagens.filter(col("id_colecao").isin(colecoes_ids))

# Criando Tabela dos Atores
dim_atores = atores_personagens.select("id_ator", "ator").distinct()

# Criando Tabela dos Personagens
dim_personagens = atores_personagens.select("id_personagem", "personagem").distinct()

# Criando Tabela dos Diretores
dim_diretores = spark.read.parquet(s3_diretores).filter(col("id_colecao").isin(colecoes_ids))
dim_diretores = dim_diretores.select("id_diretor", "diretor", "id_colecao")

# Criando Tabela dos Roteiristas
dim_roteiristas = spark.read.parquet(s3_roteiristas).filter(col("id_colecao").isin(colecoes_ids))
dim_roteiristas = dim_roteiristas.select("id_roteirista", "roteirista", "id_colecao")

dados_tmdb = spark.read.parquet(filmes_tmdb_path)
dados_local = spark.read.parquet(filmes_terror_path)

dados_tmdb = dados_tmdb.dropDuplicates(["imdb_id"])
dados_local = dados_local.dropDuplicates(["imdb_id"])

# Realizar o join entre os DataFrames
dados_filmes = dados_tmdb.join(dados_local, on="imdb_id", how="inner")

# Remover duplicatas novamente após o join
dados_filmes = dados_filmes.dropDuplicates(["imdb_id"])

# Escolhendo as Colunas entre as tabelas
dados_filmes = dados_filmes.select(
    col("imdb_id"),
    col("id").alias("id_filme"),
    col("tituloprincipal").alias("titulo_principal"),
    col("titulo_original"),
    col("id_colecao"),
    col("nome_colecao"),
    col("data_lancamento"),
    col("receita"),
    col("orcamento"),
    col("genero"),
    col("notamedia").alias("nota_media"),
    col("numerovotos").alias("numero_votos")
).where(col("id_colecao").isin(colecoes_ids))

# Criando a Tabela dos Filmes (Dimensional)
dim_filme = dados_filmes.select(
    col("id_filme"),
    col("imdb_id"),
    col("id_colecao"),
    col("titulo_principal"),
    col("titulo_original")
)

# Criando a Tabela das Coleções
dim_colecao = dados_filmes.select(
    col("id_colecao"),
    col("nome_colecao")
)

dim_datas = dados_filmes.select(col("data_lancamento"))

# Criar a Tabela de Datas
dim_datas = dim_datas.withColumn("ano", year("data_lancamento")) \
    .withColumn("mes", month("data_lancamento")) \
    .withColumn("dia", dayofmonth("data_lancamento")) \
    .withColumn("decada", (year("data_lancamento") / 10).cast("int") * 10)

# Gerar ID único para cada data
dim_datas = create_unique_ids(dim_datas, "data_lancamento", "id_data")

# Criar a Tabela de Fatos com a relação entre atores e personagens
fato_filmes = dados_filmes \
    .join(atores_personagens, "id_colecao", "left") \
    .join(dim_diretores, "id_colecao", "left") \
    .join(dim_roteiristas, "id_colecao", "left") \
    .join(dim_datas, "data_lancamento", "left")

fato_filmes = fato_filmes.select(
    col("id_filme"),
    col("id_ator"),
    col("id_personagem"),
    col("id_diretor"),
    col("id_roteirista"),
    col("id_data"),
    col("orcamento"),
    col("receita"),
    col("nota_media"),
    col("numero_votos")
)

# Enviando os parquets para o bucket S3

# Dimensional Atores
dim_atores = dim_atores.dropDuplicates()
dim_atores.write.mode("overwrite").parquet(atores_path)

# Dimensional Personagens
dim_personagens = dim_personagens.dropDuplicates()
dim_personagens.write.mode("overwrite").parquet(personagens_path)

# Dimensional Diretores
dim_diretores = dim_diretores.select("id_diretor", "diretor")
dim_diretores = dim_diretores.dropDuplicates()
dim_diretores.write.mode("overwrite").parquet(diretores_path)

# Dimensional Roteiristas
dim_roteiristas = dim_roteiristas.select("id_roteirista", "roteirista")
dim_roteiristas = dim_roteiristas.dropDuplicates()
dim_roteiristas.write.mode("overwrite").parquet(roteiristas_path)

# Dimensional Datas
dim_datas = dim_datas.dropDuplicates()
dim_datas.write.mode("overwrite").parquet(datas_path)

# Dimensional Filmes
dim_filme = dim_filme.dropDuplicates()
dim_filme.write.mode("overwrite").parquet(filmes_path)

# Dimensional Coleções
dim_colecao = dim_colecao.dropDuplicates()
dim_colecao.write.mode("overwrite").parquet(colecao_path)

# Fato Filmes
fato_filmes = fato_filmes.dropDuplicates()
fato_filmes.write.mode("overwrite").parquet(fato_path)