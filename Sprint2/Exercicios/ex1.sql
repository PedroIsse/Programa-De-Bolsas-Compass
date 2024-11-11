SELECT * -- Seleciona todas as tabelas
FROM livro -- Tabela principal livro
WHERE publicacao > '2014-12-31' -- Condição: Só mostrara os livros que foram publicados depois do dia 31 de Dezembro de 2014
ORDER BY cod -- Ordenado de forma crescente pela coluna "cod"