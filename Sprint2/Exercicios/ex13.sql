SELECT
    cdpro, -- Seleciona as colunas cdpro, nmcanalvendas, nmpro e quantidade_vendas (tbvendas)
    nmcanalvendas,
    nmpro, 
    SUM(qtd) AS quantidade_vendas -- Soma a quantidade total de itens vendidos
FROM tbvendas -- Da tabela tbvendas
WHERE status = 'Concluído' -- Condição: Venda ter sido concluída
GROUP BY nmcanalvendas, cdpro -- Agrupa por código do produto e nome do canal de vendas (Sem repetições)
ORDER BY quantidade_vendas -- Ordena por quantidade_vendas (Menor para o Maior)