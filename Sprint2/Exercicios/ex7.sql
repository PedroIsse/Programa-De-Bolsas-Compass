SELECT
    autor.nome -- Seleciona a coluna nome da tabela autor
FROM autor -- Tabela principal: autor
LEFT JOIN livro -- Junção a esquerda (autor -> livro)
    ON autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
WHERE livro.cod IS NULL -- Condição: Coluna cod (livro) deve ser nula, para ser considerada
ORDER BY autor.nome -- Ordenado pelo nome (autor) (Ordem alfabética)