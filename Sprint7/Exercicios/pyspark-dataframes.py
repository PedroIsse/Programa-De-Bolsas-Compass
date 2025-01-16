import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, desc, count, sum

# Parâmetros do job: Nome, caminho de entrada e saída no S3
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler o arquivo CSV do S3
s3_input_path = args['S3_INPUT_PATH']
df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(s3_input_path)

# Imprimir o schema do DataFrame
df.printSchema()

# Alterar valores da coluna "nome" para maiúsculo
df = df.withColumn("nome", upper(col("nome")))

# Imprimir a contagem de linhas presentes no DataFrame
print(f"Total de linhas no DataFrame: {df.count()}")

# Contagem de nomes agrupados por "ano" e "sexo", ordenados pelo ano mais recente
df_agrupado = df.groupBy("ano", "sexo").agg(count("nome").alias("total_nomes"))
df_agrupado.orderBy(desc("ano")).show()

# Nome feminino com mais registros e o ano
fem_maximo = df.filter(col("sexo") == "F").orderBy(desc("total")).select("nome", "ano", "total")
fem_maximo.show(1)

# Nome masculino com mais registros e o ano
masc_maximo = df.filter(col("sexo") == "M").orderBy(desc("total")).select("nome", "ano", "total")
masc_maximo.show(1)

# Total de registros por ano (primeiras 10 linhas, ordenadas pelo ano de forma crescente)
df_total_registros = df.groupBy("ano").agg(sum("total").alias("total_ano"))
df_total_registros.orderBy("ano").limit(10).show()

# Salvar os dados no S3 em formato JSON, particionando por sexo e ano
s3_target_path = args['S3_TARGET_PATH']
df.write.mode("overwrite").partitionBy("sexo", "ano").json(s3_target_path)

# Commit do job
job.commit()