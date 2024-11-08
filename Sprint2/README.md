# **Resumo**

### **SQL para Análise de Dados: Do básico ao avançado**

### **Big Data**

### **Ciência de Dados**

### **Tipo de Dados**

### **Banco de Dados**

### **Tipo de Armazenamentos**

### **Data Lake**

### **Técnicas de Processamento de Dados**

### **Business Intelligence (BI)**

### **Data Warehouse (DW)**

### **Mineração de Dados**

### **Machine Learning**

### **Deep Learning**

### **Relatórios e Dashboards**

### **Internet of Things (IoT)**

### **APIs**

### **Métodos de acesso à Banco de Dados**

### **ELT e ETL**

### **Normalização e Modelagem Relacional**

### **Modelagem Dimensional**

### **AWS Skill Builder - AWS Partner: Sales Accreditation**

# Exercícios

[**Exercício 1**](../Sprint2/Exercicios/ex1.sql): *"Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma"*

[**Exercício 2**](../Sprint2/Exercicios/ex2.sql): *Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.*

[**Exercício 3**](../Sprint2/Exercicios/ex3.sql): *Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.*

[**Exercício 4**](../Sprint2/Exercicios/ex4.sql): *Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*

[**Exercício 5**](../Sprint2/Exercicios/ex5.sql): *Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.*

[**Exercício 6**](../Sprint2/Exercicios/ex6.sql): *Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.*

[**Exercício 7**](../Sprint2/Exercicios/ex7.sql): *Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.*

[**Exercício 8**](../Sprint2/Exercicios/ex8.sql): *Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.*

[**Exercício 9**](../Sprint2/Exercicios/ex9.sql): *Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.*

[**Exercício 10**](../Sprint2/Exercicios/ex10.sql): *A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor.* 

*Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.*

*As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.*

[**Exercício 11**](../Sprint2/Exercicios/ex11.sql): *Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente*

[**Exercício 12**](../Sprint2/Exercicios/ex12.sql): *Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.*


*Observação: Apenas vendas com status concluído.*

[**Exercício 13**](../Sprint2/Exercicios/ex13.sql): *Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*

[**Exercício 14**](../Sprint2/Exercicios/ex14.sql): *Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.*

*Observação: Apenas vendas com status concluído.*

[**Exercício 15**](../Sprint2/Exercicios/ex15.sql): *Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.*

[**Exercício 16**](../Sprint2/Exercicios/ex16.sql): *Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).*

*Obs: Somente vendas concluídas.*

___

# **Evidências**

## **Resultado Exercícios:**

**Exercício 1:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 2:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 3:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 4:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 5:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 6:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 7:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 8:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 9:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 10:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 11:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 12:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 13:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 14:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 15:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem

**Exercício 16:** Ao executar a query no SQLiteStudio foi obitido o seguinte resultado:

-- Imagem 

Que, consequentemente, ao colocar no Compilador da Udemy gerou o mesmo resultado, assim fazendo com que o exercício configurasse como "Sucesso":

-- Imagem
___

# **Certificados**

[***Certificado do Curso: AWS Skill Builder - AWS Partner: Sales Accreditation****](../Assets/)


