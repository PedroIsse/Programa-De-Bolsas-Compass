with vendas_total as ( -- Cria uma subquery (CTE)
    select
        tbvendedor.cdvdd, -- Seleciona a coluna cdvdd da tabela tbvendedor
        tbvendedor.nmvdd as vendedor, -- Seleciona a coluna nmvdd da tabela tbvendedor
        sum(qtd * vrunt) as valor_total_vendas, -- Faz a soma total das vendas
        round(sum(qtd * vrunt) * perccomissao/ 100, 2) as comissao -- Faz a soma total das vendas, depois calcula a comissao
    from tbvendas -- Tabela principal tbvendas
    left join tbvendedor -- Junção a esquerda (tbvendas -> tbvendedor)
        on tbvendas.cdvdd = tbvendedor.cdvdd -- Condição de junção: as colunas tbvendas.cdvdd e tbvendedor.cdvdd devem corresponder
    where tbvendas.status <> 'Em aberto' and tbvendas.status <> 'Cancelado' -- Condição: O status da venda precisa estar Concluido
    group by tbvendedor.cdvdd, tbvendedor.nmvdd -- Agrupado por Código do Vendedor e Nome do vendedor
)

select
    vendedor, -- Seleciona as colunas vendedor, valor_total_vendas e comissao
    valor_total_vendas,
    comissao
from vendas_total -- Da tabela vendas_total (Subquery CTE)
order by comissao desc; -- Ordenado por comissao (Maior para o menor valor)