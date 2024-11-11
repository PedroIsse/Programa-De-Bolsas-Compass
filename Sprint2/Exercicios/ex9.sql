SELECT
    cdpro, -- Seleciona as colunas cdpro e nmpro (SUBQUERY: vendas_data)
    nmpro
FROM (
    SELECT
        *,
        SUM(tbvendas.cdpro)/tbvendas.cdpro AS max_produto -- Soma toda as aparições do código do produto e depois divide por ele mesmo, para saber quantas vezes aparece
    FROM tbvendas -- Tabela: tbvendas
    WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02' -- Condição: Somente produtos entre as datas '2014-02-03' e '2018-02-02'
    GROUP BY tbvendas.cdpro -- Agrupado por tbvendas.cdpro (Código de produto) (Sem repetições)
    ORDER BY max_produto desc -- Ordenado pelo produto (Maior para Menor)
    LIMIT 1 -- Apenas a primeira linha
) AS vendas_data -- Subquery criada para resolução