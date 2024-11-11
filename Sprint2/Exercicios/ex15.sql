SELECT
    cdven -- Seleciona a coluna cdven
FROM tbvendas -- Da tabela tbvendas
WHERE deletado > 0 -- Condição: valor na coluna deletado ser maior que 0
ORDER BY cdven -- Ordena por código de venda (Menor para o maior)