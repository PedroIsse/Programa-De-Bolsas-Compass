#!/bin/bash

# Cria uma variável para receber o caminho do diretório a ser criado, vendas
pathVendas="/home/pedro/vendas"

# Verifica se o diretório vendas já existe; caso não, é criado
mkdir -p "$pathVendas"

# Cria uma variável para receber o caminho do arquivo dados_de_vendas.csv
pathDadosVendas="/home/pedro/ecommerce/dados_de_vendas.csv"

# Copia o arquivo para o diretório vendas
cp "$pathDadosVendas" "$pathVendas"

# Cria uma variável que recebe o caminho do diretório de backup
pathBackup="$pathVendas/backup"

# Verifica se o diretório backup já existe; caso não, é criado
mkdir -p "$pathBackup"

# Gera a data no formato yyyymmdd
data=$(date +"%Y%m%d")

# Copia o arquivo para o diretório backup com a data no nome
cp "$pathDadosVendas" "$pathBackup/dados-$data.csv"

# Renomeia o arquivo para backup-dados-<data>.csv
mv "$pathBackup/dados-$data.csv" "$pathBackup/backup-dados-$data.csv"

# Obtendo a primeira data
primeira_data=$(head -n 1 "$pathDadosVendas" | awk -F, '{print $5}' | xargs)

# Obtendo a última data
ultima_data=$(tail -n 1 "$pathDadosVendas" | awk -F, '{print $5}' | xargs)

# Calculando a quantidade total de produtos diferentes vendidos
tipo_produtos=$(awk -F, '{print $2}' "$pathDadosVendas" | sort | uniq | wc -l)

# Pega as 10 primeiras linhas do backup-dados-<yyyymmdd>.csv
dezLinhas=$(head -n 10 "$pathBackup/backup-dados-$data.csv") 

# Cria o relatório no arquivo relatorio-$data.txt
{
    echo "Data do sistema: $(date +"%Y/%m/%d %H:%M")"
    echo "Primeira data: $primeira_data"
    echo "Última data: $ultima_data"
    echo "Quantidade total de produtos diferentes vendidos: $tipo_produtos"
    echo "Primeiras 10 linhas do backup: "
    echo "$dezLinhas"
} > "$pathBackup/relatorio-$data-teste.txt"

# Zipando o arquivo backup-dados-<yyyymmdd>.csv
zip -r "$pathBackup/backup-dados-$data.zip" "$pathBackup/backup-dados-$data.csv"

# Excluindo dados_de_vendas.csv e backup-dados-<yyyymmdd>.csv do diretório vendas
rm "$pathVendas/dados_de_vendas.csv"
rm "$pathBackup/backup-dados-$data.csv"
