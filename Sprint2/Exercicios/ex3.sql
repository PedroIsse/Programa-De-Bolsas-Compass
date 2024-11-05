select
    count(*) as quantidade, -- Cria a coluna "quantidade" que somara todos os livros
    editora.nome, -- Seleciona a coluna nome da tabela editora
    endereco.estado, -- Seleciona a coluna estado da tabela endereco
    endereco.cidade -- Seleciona a coluna cidade da tabela endereco
    
from livro -- A tabela livor é a principal
left join editora -- Junção à esquerda (livro -> editora)
    on livro.editora = editora.codeditora -- Condição de junção: as colunas editora e codeditora devem corresponder
left join endereco -- Junção à esquerda (editora -> endereco)
    on editora.endereco = endereco.codendereco -- Condição de junção: as colunas endereco e codendereco devem corresponder
group by editora.nome -- Agrupado pelo nome das editoras, para que haja redução de linhas
order by quantidade desc -- Ordena por quantidade descrescente de livros por editora