import pyspark 
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

# Etapa 1

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt")

df_nomes.show(5)

# Etapa 2

df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.show(10)

# Etapa 3

from pyspark.sql.functions import when, rand

df_nomes = df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental").when(rand() > 0.66, "Médio").otherwise("Superior"))

df_nomes.show(10)

# Etapa 4

paises = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Ecuador", 
    "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 1/13, paises[0])
    .when(rand() < 2/13, paises[1])
    .when(rand() < 3/13, paises[2])
    .when(rand() < 4/13, paises[3])
    .when(rand() < 5/13, paises[4])
    .when(rand() < 6/13, paises[5])
    .when(rand() < 7/13, paises[6])
    .when(rand() < 8/13, paises[7])
    .when(rand() < 9/13, paises[8])
    .when(rand() < 10/13, paises[9])
    .when(rand() < 11/13, paises[10])
    .when(rand() < 12/13, paises[11])
    .otherwise(paises[12])
)

df_nomes.show(10)

# Etapa 5

ano_inicio = 1945
ano_fim = 2010

df_nomes = df_nomes.withColumn("Ano", (rand() * (ano_fim - ano_inicio + 1) + ano_inicio).cast("int"))

df_nomes.show(10)

# Etapa 6

from pyspark.sql.functions import col

df_select = df_nomes.select("Nomes").where(col('Ano') > 2000)

df_select.show(10)

# Etapa 7 

df_nomes.createOrReplaceGlobalTempView("pessoas")

spark.sql("SELECT Nomes FROM global_temp.pessoas WHERE Ano > 2000").show()

# Etapa 8

df_nomes.filter((col("Ano") > 1979) & (col("Ano") < 1995)).count()

# Etapa 9 

spark.sql("SELECT count(*) as Millennials FROM global_temp.pessoas WHERE Ano > 1979 AND Ano < 1995").show()

# Etapa 10

df_resultado = spark.sql("""
    SELECT 
        Pais,
        CASE
            WHEN Ano < 1965 THEN 'Baby Boomers'
            WHEN Ano < 1980 THEN 'Geração X'
            WHEN Ano < 1995 THEN 'Millennials (Geração Y)'
            ELSE 'Geração Z'
        END AS Geracao,  
        COUNT(*) AS Quantidade
    FROM global_temp.pessoas
    GROUP BY Pais, 
        CASE 
            WHEN Ano < 1965 THEN 'Baby Boomers'
            WHEN Ano < 1980 THEN 'Geração X'
            WHEN Ano < 1995 THEN 'Millennials (Geração Y)'
            ELSE 'Geração Z'
        END
    ORDER BY Pais, Quantidade, 
        CASE 
            WHEN Ano < 1965 THEN 'Baby Boomers'
            WHEN Ano < 1980 THEN 'Geração X'
            WHEN Ano < 1995 THEN 'Millennials (Geração Y)'
            ELSE 'Geração Z'
        END
""")

df_resultado.show(52)