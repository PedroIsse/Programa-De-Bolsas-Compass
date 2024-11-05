select
    cdven -- Seleciona a coluna cdven
from tbvendas -- Da tabela tbvendas
where deletado > 0 -- Condição: valor na coluna deletado ser maior que 0
order by cdven -- Ordena por código de venda (Menor para o maior)