SELECT
    tbvendedor.nmvdd AS vendedor, -- Seleciona as tabelas vendedor (tbvendedor.nmvdd renomeada), valor_total_vendas e comissao
    SUM(qtd * vrunt) AS valor_total_vendas, -- Faz a soma total de vendas (Quantidade vezes Valor Unitário)
    ROUND(SUM(qtd * vrunt) * perccomissao/ 100, 2) AS comissao -- Faz a soma total de vendas, depois calcula a comissão (Arredonda em 2 casas) 
FROM tbvendas -- Tabela principal: tbvendas
LEFT JOIN tbvendedor -- Junção a esquerda (tbvendas -> tbvendedor)
    ON tbvendas.cdvdd = tbvendedor.cdvdd -- Condição de junção: as colunas tbvendas.cdvdd e tbvendedor.cdvdd devem corresponder
WHERE tbvendas.status <> 'Em aberto' AND tbvendas.status <> 'Cancelado' -- Condição: O status da venda precisa estar Concluido
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd -- Agrupado por Código do Vendedor e Nome do vendedor (Sem repetições)
ORDER BY comissao DESC -- Ordenado por comissao (Maior para o menor)