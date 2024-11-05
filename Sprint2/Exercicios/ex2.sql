select
    titulo, -- Seleciona coluna titulo
    valor -- Seleciona coluna valor

from livro -- Tabela principal: livro
where (select max(valor) from livro) -- Condição: Uso uma subquery para achar o valor MÁXIMO da coluna "valor" da tabela "livro"
order by valor desc -- Ordeno pela coluna "valor", por ordem decrescente
limit 10-- Mostra somente os 10 primeiros valores que atendem a condição