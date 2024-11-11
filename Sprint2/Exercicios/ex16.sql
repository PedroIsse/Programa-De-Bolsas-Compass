SELECT
    estado, -- Seleciona as colunas estado, nmpro e quantidade_media (tbvendas)
    nmpro,
    ROUND(SUM(qtd * 1.0) / COUNT(*), 4) AS quantidade_media -- Converte a soma das quantidades e divide pelo total de vezes que aparece a combinação de estado e produto (Arredonda para 4 casas)
FROM tbvendas -- Da tabela tbvendas
WHERE status = 'Concluído' -- Condição: status precisa estar Concluído
GROUP BY estado, nmpro -- Agrupa por estado e nome do produto (Sem repetições)
ORDER BY estado, nmpro -- Ordena por estado e nome do produto (Ordem alfabética)