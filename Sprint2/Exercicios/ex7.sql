select 
    autor.nome -- Seleciona a coluna nome da tabela autor
from autor -- Autor é a tabela principal 
left join livro -- Junção a esquerda (autor -> livro)
    on autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
where livro.cod is null -- Se a coluna "cod" estiver nula, significa que o autor não tem livro publicado, e deve ser mostrado na tabela
order by autor.nome -- Ordenado pelo nome (ordem alfabética)