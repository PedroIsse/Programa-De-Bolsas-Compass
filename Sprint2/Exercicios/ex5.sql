select 
    autor.nome -- Seleciona a coluna nome da tabela autor
from autor -- Autor é a tabela principal 
left join livro -- Junção a esquerda (autor -> livro)
    on autor.codautor = livro.autor -- Condição de junção: as colunas codautor e autor devem corresponder
left join editora -- Junção a esquerda (livro -> editora)
    on livro.editora = editora.codeditora -- Condição de junção: as colunas editora e codeditora devem corresponder
left join endereco -- Junção a esquerda (editora -> endereco)
    on editora.endereco = endereco.codendereco -- Condição de junção: as colunas endereco e codendereco devem corresponder
where 
    endereco.estado not in ('RIO GRANDE DO SUL', 'PARANÁ') -- Só serão mostrados aqueles que a editora não é no Sul
group by autor.nome -- Agrupado por nome
order by autor.nome -- Ordenado por nome (ordem alfabética)