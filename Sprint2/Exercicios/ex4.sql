SELECT 
    autor.nome, -- Seleciona as colunas nome (autor), codautor (autor), nascimento (autor) e autor (livro)
    autor.codautor,
    autor.nascimento,
    count(livro.autor) AS quantidade -- Conta quantos livros os autores publicaram
FROM autor -- Tabela principal: autor
LEFT JOIN livro -- Junção à esquerda (autor -> livro) 
    ON autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
GROUP BY autor.nome -- Agrupa pelo nome do autor (Sem repetições)
ORDER BY autor.nome -- Ordena pelo nome do autor (Ordem alfabética)

