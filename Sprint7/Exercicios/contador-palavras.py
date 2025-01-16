from pyspark import SparkContext

sc = SparkContext(appName="ContagemPalavras")

path = 'README.md'

rdd = sc.textFile(path)

palavras = rdd.flatMap(lambda line: line.split())

palavras_sep = palavras.collect()

frequencia = {}

for palavra in palavras_sep:

    palavra = palavra.lower()

    if palavra in frequencia.keys():
            frequencia[palavra] += 1
    else:
            frequencia[palavra] = 1

for palavra, aparicoes in frequencia.items():
    print(f'{palavra}: {aparicoes}')