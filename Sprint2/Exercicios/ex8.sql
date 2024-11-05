select
    cdvdd, -- Seleciona as colunas cdvdd e nmvdd
    nmvdd
from (
    select
        *,
        sum(tbvendas.cdvdd)/tbvendas.cdvdd as max_vendas -- Soma toda as aparições do código do vendedor e depois divide por ele mesmo, para saber quantas vezes aparece
    from tbvendas -- Da tabela vendas
    left join tbvendedor -- Junção a esquerda (tbvenda -> tbvendedor)
        on tbvendas.cdvdd = tbvendedor.cdvdd  -- Condição de junção: as colunas tbvendas.cdvdd e tbvendedor.cdvdd devem corresponder
    group by tbvendas.cdvdd -- Agrupados por código do vendedor
    order by max_vendas desc -- Ordenado pelo Maior Número de vendas
    limit 1 -- Apenas a primeira linha
) as vendedor_mais_vendas -- Tabela principal vendedor_mais_vendas (SUBQUERY FROM)