SELECT
    estado, -- Seleciona coluna estado e gastomedio (tbvendas)
    ROUND(SUM(qtd * vrunt * 1.0) / COUNT(*), 2) AS gastomedio -- Faz o produto de quantidade e valor unitário (1.0 para converter para float), soma todos e divide pela quantidade vezes que o estado aparece
FROM tbvendas -- Tabela principal: tbvendas
WHERE status = 'Concluído' -- Condição: somente vendas com status concluído
GROUP BY estado -- Agrupado por estado (Sem repetições)
ORDER BY gastomedio DESC -- Ordenado por gastomedio (Maior para o menor)