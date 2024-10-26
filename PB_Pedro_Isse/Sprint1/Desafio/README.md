# Desafio - Sprint 1

## Entendimento do Desafio

Quando recebi o desafio, a primeira coisa que fiz foi tentar entender ele, para que assim, ao decorrer dos Cursos fornecidos na trilha eu já soubesse o que eu teria que me atentar mais para que eu não tivesse grandes dificuldades durante a resolução do desafio.

![DiagramaEstruturaDesafio](/Assets/ProcessamentoDeVendas.drawio.png)

1. Crio um diretório chamado de [ecommerce](/PB_Pedro_Isse/Sprint1/Desafio/ecommerce)
    - Nele adiciono o arquivo [dados_de_vendas.csv](/PB_Pedro_Isse/Sprint1/Desafio/ecommerce/dados_de_vendas.csv)

2. Agora começo o desenvolvimento do primeiro script [processamento_de_vendas.sh](/PB_Pedro_Isse/Sprint1/Desafio/processamento_de_vendas.sh)

    - Nele será desenvolvido relatórios que serão gerados de segunda a quinta-feira, entretanto, no meu foi executado de terça a sexta-feira, pois meu script foi finalizado segundo, porém, depois das 15:27, que é o horário que deve ser executado.

    - Quando for executado ele criará uma estrutura de diretórios, que é o diretório [vendas](/PB_Pedro_Isse/Sprint1/Desafio/vendas) e seu subdiretório [backup](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/)

    - Será copiado para o diretório de [vendas](/PB_Pedro_Isse/Sprint1/Desafio/vendas) o arquivo [dados_de_vendas.csv](/PB_Pedro_Isse/Sprint1/Desafio/ecommerce/dados_de_vendas.csv) do diretório [ecommerce](/PB_Pedro_Isse/Sprint1/Desafio/ecommerce). Logo em seguida a cópia será transferida para o diretório [backup](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup) com o nome dados-<data_de_execução> e depois será renomeado para backup-dados-<data_de_execução>

    - A partir desse ponto, o relatório do dia será gerado, contendo as seguintes informações: 
        - Data de execução do programa no formato YYYY/MM/DD H:M
        - Data da primeira venda realizada
        - Data da última venda realizada
        - As 10 primeiras linhas do arquivo backup-dados-<data_de_execução>, para gerar uma espécie de log do arquivo

     Assim, gerando um arquivo chamado de relatorio-<data_de_execução>, que será armazenado no diretório [backup](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup), aqui estão os arquivos gerados durante a resolução da Sprint
        - [Relatório 2024/10/22](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/relatorio-20241022.txt)
        - [Relatório 2024/10/23](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/relatorio-20241023.txt)
            - Esse relatório está com a última data vazia, pois na sua execução o arquivo [dados_de_vendas.csv](/PB_Pedro_Isse/Sprint1/Desafio/ecommerce/dados_de_vendas.csv) tinha uma linha vazia abaixo dos itens vendidos, assim puxando o contéudo ou falta de coutéudo dela, ao invés da data da última venda.
        - [Relatório 2024/10/24](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/relatorio-20241024.txt)
        - [Relatório 2024/10/25](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/relatorio-20241025.txt)

    - Por fim, para garantir que a quantidade arquivos gerados não ocupe tanto espaço do disco os arquivos backup-dados-<data_de_execução> são compactados. Os arquivos de backups compactados na pasta [backup](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup):
        - [Backup de dados 2024/10/22](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/backup-dados-20241022.zip)
        - [Backup de dados 2024/10/23](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/backup-dados-20241023.zip)
        - [Backup de dados 2024/10/24](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/backup-dados-20241024.zip)
        - [Backup de dados 2024/10/25](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/backup-dados-20241025.zip)
    
    - Depois são removidos os arquivos de backup-dados-<data_de_execução>.csv do diretório [backup](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup) e o arquivo dados_de_vendas.csv do diretório [vendas](/PB_Pedro_Isse/Sprint1/Desafio/vendas)

3. Agora para o desenvolvimento do scrip [consolidador_de_processos.sh](/PB_Pedro_Isse/Sprint1/Desafio/consolidador_de_processamento.sh). O objetivo dele é juntar os relatóris criados no diretório [backup](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup) e juntar em arquivo chamado [relatorio_final.txt](/PB_Pedro_Isse/Sprint1/Desafio/vendas/backup/relatorio_final.txt)

## Funcionamento dos scripts

#### Scrip 1 - processamento_de_vendas.sh

'''shell
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
'''

##### Explicando principais comandos

- **Criação de variáveis**: As variáveis que começam com 'path' recebem caminhos absolutos para diretórios ou arquivos. As outras recebem alguma informação, a variável data recebe a data do Sistema Operacional, por exemplo;

- **Utilização do $**: Concatena o conteúdo da variável que estiver acompanhando;

- **mkdir -p**: Cria um diretório, mas quando está com a flag '-p' ele verifica se o diretório já existe, caso exista ele **não** irá substituir o diretório já existente por outro, assim evitando perda de conteúdo;

- **cp**: Copia um arquivo ou diretório para outro diretório;

- **date**: Encontra a data atual do Sistema Operacional Linux;

- **mv**: Renomeia ou move um arquivo ou diretório para outro;

- **head -n**: Pega o conteúdo do número de linhas pedido, de cima para baixo;

- **tail -n**: Pega o conteúdo do número de linhas pedido, de baixo para cima;

- **awk -F**: Usa para delimitador da campos, a flag -F faz com que o delimitador considerado seja a vírgula;

- **sort**: Organiza uma lista em ordem alfabética;

- **uniq**: Remove linhas duplicadas;

- **wc -l**: Conta o número de linhas de um arquivo;

- **zip**: Compacta um arquivo no formato <nome>.zip;

- **rm**: Remove arquivo.

#### Scrip 2 - consolidador_de_processos.sh

'''shell
    #!/bin/bash

    # Crio um caminho para o diretório de backup e já nomeio o futuro arquivo do relatório final
    pathRelatorios="/home/pedro/vendas/backup"
    relatorioFinal="relatorio_final.txt"

    # Utiliza a variável pathRelatorios para encontrar todos os arquivos que
    # tenham relatorio no nome, para isso uso o wildcard. Por fim é criado o 
    # relatorio_final.txt que recebera a concatenção dos outros relatórios
    cat "$pathRelatorios"/relatorio* > "$pathRelatorios/$relatorioFinal"
'''

##### Explicando principais comandos

- **Criação de variáveis**: As variáveis que começam com 'path' recebem caminhos absolutos para diretórios ou arquivos. As outras recebem alguma informação, a variável data recebe a data do Sistema Operacional, por exemplo;

- **Utilização do $**: Concatena o conteúdo da variável que estiver acompanhando;

- **cat**: Serve para mostrar o conteúdo de um arquivo para 

