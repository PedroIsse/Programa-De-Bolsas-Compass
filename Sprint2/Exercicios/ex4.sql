select  
    autor.nome, -- Seleciona a coluna nome da tabela autor
    autor.codautor, -- Seleciona a coluna codautor da tabela autor
    autor.nascimento, -- Seleciona a coluna nascimento da tabela autor
    count(livro.autor) as quantidade -- Faz a contagem de quantos livros cada autor escreveu, que estão presente no banco de dados 
from autor -- A tabela autor é a principal
left join livro -- Junção à esquerda (autor -> livro)
    on autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
group by autor.nome -- Agrupado pelo nome do autor
order by autor.nome -- Ordenado por nome do autor (Ordem alfabética)