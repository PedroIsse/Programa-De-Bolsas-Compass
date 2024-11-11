SELECT 
    autor.nome -- Seleciona a coluna nome (autor)
FROM autor -- Tabela principal: autor
LEFT JOIN livro -- Junção a esquerda (autor -> livro)
    ON autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
LEFT JOIN editora -- Junção a esquerda (livro -> editora)
    ON livro.editora = editora.codeditora -- Condição de junção: as colunas editora e codeditora devem corresponder
LEFT JOIN endereco -- Junção a esquerda (editora -> endereco)
    ON editora.endereco = endereco.codendereco -- Condição de junção: as colunas endereco e codendereco devem corresponder
WHERE endereco.estado not in ('RIO GRANDE DO SUL', 'PARANÁ') -- Condição: Só serão considerados aqueles que a editora não é localizada no Sul
GROUP BY autor.nome -- Agrupado por nome (Sem repetições)
ORDER BY autor.nome -- Ordenado por nome (Ordem alfabética)
