#!/bin/bash

# Crio um caminho para o diretório de backup e já nomeio o futuro arquivo do relatório final
pathRelatorios="/home/pedro/vendas/backup"
relatorioFinal="relatorio_final.txt"

# Utiliza a variável pathRelatorios para encontrar todos os arquivos que
# tenham relatorio no nome, para isso uso o wildcard. Por fim é criado o 
# relatorio_final.txt que recebera a concatenção dos outros relatórios
cat "$pathRelatorios"/relatorio* > "$pathRelatorios/$relatorioFinal"

