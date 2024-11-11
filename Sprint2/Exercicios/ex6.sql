SELECT
    autor.codautor, -- Seleciona as colunas codautor (autor), nome (autor) e quantidade_publicacoes
    autor.nome,
    SUM(livro.autor)/autor.codautor AS quantidade_publicacoes -- Soma o número de vezes que o código do autor aparece, em seguida é divido pelo código do autor, para que assim, descubra o número exato de publicações
FROM autor -- Tabela principal: autor
LEFT JOIN livro -- Junção a esquerda (autor -> livro)
    ON autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
GROUP BY autor.codautor, autor.nome -- Agrupado por código do autor (autor) e nome (autor) (Sem repetições)
ORDER BY quantidade_publicacoes desc -- Ordenado por quantidade_publicacoes (Maior para o Menor)
LIMIT 1 -- Mostra somente a primeira linha