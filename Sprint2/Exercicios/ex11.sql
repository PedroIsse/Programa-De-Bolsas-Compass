SELECT
    cdcli, -- Seleciona as colunas cdcli, nmcli e gasto (tbvendas)
    nmcli,
    SUM(qtd * vrunt) AS gasto -- Soma o gasto (Quantidade vezes Valor Unitário)
FROM tbvendas -- Da tabela tbvendas
GROUP BY cdcli -- Agrupado pelo cdcli (Código do Cliente) (Sem repetições)
ORDER BY gasto DESC -- Ordenado por gasto (Maior para Menor)
LIMIT 1 -- Mostra somente a primeira linha