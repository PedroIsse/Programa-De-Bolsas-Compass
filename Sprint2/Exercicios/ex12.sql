SELECT
    tbdependente.cddep, -- Seleciona as colunas cddep, nmdep, dtnasc e valor_total_vendas (tbdependente)
    tbdependente.nmdep,
    tbdependente.dtnasc,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas -- Soma o total de vendar por vendedor (Quantidade vezes Valor Unitário)
FROM tbvendas -- Tabela principal: tbvendas
LEFT JOIN tbdependente -- Junção a esquerda (tbvendas -> tbdependente)
    ON tbvendas.cdvdd = tbdependente.cdvdd -- Condição de junção: as colunas tbvendas.cdvdd e tbdependente.cdvdd devem corresponder
WHERE tbvendas.status = 'Concluído' -- Condição: Somente as vendas que já foram concluídas
GROUP BY tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc -- Agrupado por cddep, nmdep e dtnasc da tbdependente (Sem repetição)
ORDER BY valor_total_vendas -- Ordenado pelo valor_total_vendas (Menor para o Maior)
LIMIT 1 -- Mostra apenas a primeira linha