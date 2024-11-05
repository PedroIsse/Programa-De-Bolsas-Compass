select
    cdpro, -- Seleciona as colunas cdpro, nmcanalvendas, nmpro e quantidade_vendas
    nmcanalvendas,
    nmpro, 
    quantidade_vendas
from (
    select
        cdpro, -- Seleciona as colunas cdpro, nmcanalvendas, nmpro e quantidade_vendas
        nmcanalvendas,
        nmpro,
        sum(qtd) as quantidade_vendas -- Soma a quantidade total de itens vendidos
    from tbvendas -- Da tabela tbvendas
    where status = 'Concluído' -- Condição: Venda ter sido concluída
    group by nmcanalvendas, cdpro -- Agrupa por código do produto e nome do canal de vendas
    order by quantidade_vendas -- Ordena por quantidade_vendas (Menor para o Maior)
) as dez_produtos -- Tabela dez_produtos (SUBQUERY FROM)