-- Seleciona todas as colunas
select *

from livro -- Tabela principal livro
where publicacao > '2014-12-31' -- Condição: Só mostrara os livros que foram publicados depois do dia 31 de Dezembro de 2014
order by cod -- Ordenado de forma crescente pela coluna "cod"