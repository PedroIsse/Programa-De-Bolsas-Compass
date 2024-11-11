SELECT
    titulo, -- Selecionado as colunas titulo e valor
    valor
FROM livro -- Da tabela livro
WHERE (SELECT MAX(valor) FROM livro) -- Condição: Escolher os maiores valores da tabela livro (Livros mais caros)
ORDER BY valor DESC -- Ordena de maior para menor valor
LIMIT 10 -- Mostra as 10 primeiras linhas