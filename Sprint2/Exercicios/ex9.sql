select
    cdpro, -- Seleciona as colunas cdpro e nmpro
    nmpro
from (
    select 
        *,
        sum(tbvendas.cdpro)/tbvendas.cdpro as max_produto -- Soma toda as aparições do código do produto e depois divide por ele mesmo, para saber quantas vezes aparece
    from tbvendas -- Da tabela tbvendas
    where dtven between '2014-02-03' and '2018-02-02' -- Condição: Somente produtos entre as datas
    group by tbvendas.cdpro -- Agrupado por tbvendas.cdpro (Código de produto)
    order by max_produto desc -- Ordenado pelo produto (maior número)
    limit 1 -- Apenas a primeira linha (O produto que mais foi vendido)
) as vendas_data -- Tabela principal vendas_data (Subquery FROM)
