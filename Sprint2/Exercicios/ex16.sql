select
    estado, -- Seleciona as colunas estado, nmpro e quantidade_media
    nmpro,
    round(sum(qtd * 1.0) / count(*), 4) as quantidade_media -- Converte a soma das quantidades e divide pelo total de vezes que aparece a combinação de estado e produto
from tbvendas -- Da tabela tbvendas
where status = 'Concluído' -- Condição: status precisa estar Concluído
group by estado, nmpro -- Agrupa por estado e nome do produto
order by estado, nmpro -- Ordena por estado e nome do produto