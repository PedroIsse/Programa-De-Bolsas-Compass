select
    cdcli, -- Seleciona as colunas cdcli, nmcli e gasto
    nmcli,
    gasto
from (
    select
        *,
        sum(qtd * vrunt) as gasto -- Soma o gasto do cliente
    from tbvendas -- Da tabela vendas
    group by cdcli -- Agrupado pelo código do cliente
    order by gasto desc -- Ordenado pelo maior gasto do cliente
    limit 1 -- Apenas mostra a primeira linha (Maior gasto)
) vendas_cliente -- Tabela principal (SUBQUERY FROM)