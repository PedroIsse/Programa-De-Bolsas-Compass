select
    autor.codautor, -- Seleciona a coluna codautor da tabela autor
    autor.nome, -- Seleciona a coluna nome da tabela autor
    sum(livro.autor)/autor.codautor as quantidade_publicacoes -- Soma o total de cada grupo dos autores (é representado pelo código)
                                                              -- Em seguida é dividido pelo código do autor para que descubra o número de publicações
from autor -- Autor é a tabela principal
left join livro -- Junção a esquerda (autor -> livro)
    on autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
group by autor.codautor, autor.nome -- Agrupado por código do autor e nome
order by quantidade_publicacoes desc -- Mostra do maior para o menor
limit 1 -- Mostra somente a primeira linha