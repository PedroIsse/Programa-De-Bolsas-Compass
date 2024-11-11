SELECT
    COUNT(*) AS quantidade, -- Seleciona as colunas quantidade (livro), nome (editora), estado (endereco) e cidade (endereco)
    editora.nome,
    endereco.estado,
    endereco.cidade
FROM livro -- Tabela principal: Livro
LEFT JOIN editora -- Junção à esquerda (livro -> editora)
    ON livro.editora = editora.codeditora -- Condição de junção: as colunas editora e codeditora devem corresponder
LEFT JOIN endereco -- Junção à esquerda (editora -> endereco)
    ON editora.endereco = endereco.codendereco -- Condição de junção: as colunas endereco e codendereco devem corresponder
GROUP BY editora.nome -- Agrupado pelo nome das editoras, para que haja redução de linhas
ORDER BY quantidade DESC -- Ordena por quantidade descrescente de livros por editora