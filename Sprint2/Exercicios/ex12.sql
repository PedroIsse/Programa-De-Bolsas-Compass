select
    cddep, -- Seleciona as colunas cddep, nmdep, dtnasc e valor_total_vendas
    nmdep,
    dtnasc,
    valor_total_vendas
from (
    select
        tbdependente.cddep, -- Seleciona as colunas cddep, nmdep e dtnasc da tabela tbdependente
        tbdependente.nmdep,
        tbdependente.dtnasc,
        sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas -- Soma o total de vendas por vendedor
    from tbvendas -- Tabela principal: tbvendas
    left join tbdependente -- Junção a esquerda (tbvendas -> tbdependente)
        on tbvendas.cdvdd = tbdependente.cdvdd -- Condição de junção: as colunas tbvendas.cdvdd e tbdependente.cdvdd devem corresponder
    where tbvendas.status = 'Concluído' -- Somente as vendas que já foram concluídas
    group by tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc -- Agrupado por cddep, nmdep e dtnasc da tbdependente
    order by valor_total_vendas -- Ordenado pelo valor_total_vendas (Menor para o Maior)
    limit 1 -- Mostra apenas a primeira linha
) as dependentes_vendedor -- Tabela dependentes_vendedor (SUBQUERY FROM)