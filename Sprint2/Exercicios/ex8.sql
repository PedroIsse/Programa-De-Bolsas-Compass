SELECT
    cdvdd, -- Seleciona as colunas cdvdd e nmvdd (SUBQUERY: vendedor_mais_vendas)
    nmvdd
FROM (
    SELECT 
        *,
        SUM(tbvendas.cdvdd)/tbvendas.cdvdd AS max_vendas -- Soma toda as aparições do vendedor, pelo seu código, e depois divide por ele mesmo, para que assim, seja possível saber quantas vezes ele aparece
    FROM tbvendas -- Tabela principal: tbvendas
    LEFT JOIN tbvendedor -- Junção a esquerda (tbvenda -> tbvendedor)
        ON tbvendas.cdvdd = tbvendedor.cdvdd -- Condição de junção: as colunas tbvendas.cdvdd e tbvendedor.cdvdd devem corresponder
    GROUP BY tbvendas.cdvdd -- Agrupado pelo código do vendedor (Sem repetições)
    ORDER BY max_vendas DESC -- Ordenado pela coluna max_vendas (Maior número de vendas)
    LIMIT 1 -- Apenas a primeira linha
) AS vendedor_mais_vendas -- Subquery criada para resolução