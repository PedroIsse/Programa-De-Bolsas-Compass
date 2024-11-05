select
    estado, -- Seleciona coluna estado e gastomedio
    round(sum(qtd * vrunt * 1.0) / count(*), 2) as gastomedio -- Faz o produto de quantidade e valor unitário (1.0 para converter para float), soma todos e divide pela quantidade vezes que o estado aparece
from tbvendas -- Tabela principal: tbvendas
where status = 'Concluído' -- Condição: somente vendas com status concluído
group by estado -- Agrupado por estado
order by gastomedio desc; -- Ordenado por gastomedio (Maior para o menor)