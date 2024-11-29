# **Resumo**

### **Programação Funcional**

**O que é:** Programação funcional é o processo de construir software através de composição de funções puras, evitando compartilhamento de estados, dados mutáveis e efeitos colaterais. ***É declarativa ao invés de Imperativa.***

**Composição de Funções:** Composição de funções é criar uma nova função através da composição de outras. Por exemplo:

```Python
# Lista de números
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para filtrar números pares
def filtrar_pares(arr):
    return filter(lambda numero: numero % 2 == 0, arr)

# Função para multiplicar números por 2
def multiplicar_por_dois(arr):
    return map(lambda numero: numero * 2, arr)

# Composição das funções
def transformar(arr):
    return list(multiplicar_por_dois(filtrar_pares(arr)))

resultado = transformar(numeros)
print(resultado)  # [4, 8, 12, 16, 20]
```

**Funções Puras:** Uma função é chamada pura quando invocada mais de uma vez produz exatamente o mesmo resultado. Isto é, o retorno da função é sempre o mesmo se você passar os mesmos parâmetros, então ela não pode depender de valores mutáveis.  Por outro lado, ela não pode causa efeitos colaterais externos, pois se ela imprime uma linha de saída, altera algo no banco, lança um foguete para o espaço, ao invocá-la a segunda vez ela vai causar um novo efeito.

```Python
def verificar_se_eh_maior(num1, num2):
    return True if num1 > num2 else False

verificar_se_eh maior(13, 12) # True
verificar_se_eh maior(12 13) # False
```

**Imutabilidade:** Imutabilidade significa que uma vez que uma variável que recebeu um valor, vai possuir esse valor para sempre, ou quando criamos um objeto ele não pode ser modificado. Em python o conceito de Imutabilidade pode ser descrito por meio dos IDs.

- **Tipos:** int, float, complex, str, tuple e bool MUDAM seu ID ao mudarem seu valor

```Python
x = 10
print(id(x))  # ID do objeto 10
x = x + 5
print(id(x))  # Novo ID porque um novo objeto foi criado
```

- **Tipos:** List, dict e set NÃO MUDAM seu ID ao mudarem seu valor (Adicionar ou Retirar conteúdo)

```Python
lista = [1, 2, 3]
print(id(lista))  # ID inicial
lista.append(4)   # Modifica a lista
print(id(lista))  # Mesmo ID, pois o objeto foi alterado
```

Entretando, utilizando funções como map, reduce e lambda para gerar novos valores sem mexer nos originais é IMUTABILIDADE.

**Efeito Colateral:** Efeito colateral é toda interação da nossa função com o mundo externo No nosso dia a dia fazemos coisas como:

- Acessar banco de dados
- Realizar chamadas assíncronas
- Alterar propriedades de objetos entre outras tarefas

Então a programação funcional não elimina efeitos colaterais totalmente, mas tentam confiná-los. Como fazemos interface com o mundo real, algumas partes do programa vão ser impuras então o papel é minimizar essas partes e separá-las do resto do programa.

**Imperativo Declarativo:** É muito comum aprender a programar de forma **imperativa**, onde mandamos alguém fazer algo. Busque o usuário 15 no banco de dados. Valide essas informações do usuário.

Na programação funcional tentamos programar de forma **declarativa**, onde declaramos o que desejamos, sem explicitar como será feito. Qual o usuário 15? Quais os erros dessas informações?

**Estado Compartilhado:** Estado compartilhado é qualquer valor que está acessível por mais de um ponto de uma aplicação. Por exemplo:

**Com variável Global:** Maior chance de ocorrer erros.
```Python
# Variável global - estado compartilhado
contador = 0

def incrementar():
    global contador  # Modifica o estado compartilhado
    contador += 1
    print(f"Contador após incremento: {contador}")

def decrementar():
    global contador  # Modifica o estado compartilhado
    contador -= 1
    print(f"Contador após decremento: {contador}")

# Chamadas às funções que compartilham o mesmo estado
incrementar()  # Contador: 1
decrementar()  # Contador: 0
incrementar()  # Contador: 1
```

**Encapsulamento da variável:** Menos erros.

```Python
class Contador:
    def __init__(self):
        self._contador = 0  # Estado encapsulado

    def incrementar(self):
        self._contador += 1
        print(f"Contador: {self._contador}")

    def decrementar(self):
        self._contador -= 1
        print(f"Contador: {self._contador}")

# Instância com estado encapsulado
contador = Contador()
contador.incrementar()  # Contador: 1
contador.decrementar()  # Contador: 0
```

### **Programação Funcional - Direcionada a Python** 

**Funções de Primeira Classe:** Em ciência da computação, dizemos que funções são de primeira classe em uma linguagem de programação quando podem ser tratadas como qualquer outro tipo de dado. (Atribuir a variáveis; Passadas como argumentos para outras funções; Retornada como resultados de outras funções; Armazenadas em estruturas de dados).

```Python
# Define uma função que retorna o dobro de um número
def dobro(x):
    return x * 2

# Define uma função que retorna o quadrado de um número
def quadrado(x):
    return x ** 2

# Cria uma lista que alterna as funções 'dobro' e 'quadrado', repetindo o padrão 5 vezes
# Exemplo: [dobro, quadrado, dobro, quadrado, ...] (10 elementos)
funcs = [dobro, quadrado] * 5

# Combina a lista de funções com uma sequência de números de 1 a 10 usando zip
for func, numero in zip(funcs, range(1, 11)):
    # Para cada par (funcão, número), chama a função com o número como argumento
    # e imprime o nome da função (usando func.__name__) e o resultado
    print(f'O {func.__name__} de {numero} é {func(numero)}')
```

**Funções de Alta Ordem:** Funções de alta ordem (ou funções de ordem superior) são aquelas que:

- Recebem uma ou mais funções como argumento.
- Retornam uma função como resultado.
- Essas funções permitem tratar funções como valores e são um componente essencial na programação funcional.

```Python
# Função que eleva ao quadrado
def quadrado(x):
    return x ** 2

# Função de alta ordem que aplica outra função a cada elemento de uma lista
def aplicar_a_lista(funcao, lista):
    return [funcao(x) for x in lista]

# Usando a função de alta ordem
numeros = [1, 2, 3, 4, 5]
resultado = aplicar_a_lista(quadrado, numeros)
print(resultado)  # Saída: [1, 4, 9, 16, 25]
```

**Closure:** É definida dentro de outra função (função interna).
Captura e "lembra" o estado de variáveis do escopo da função externa, mesmo depois que esta função externa tenha sido executada.

```Python
def multiplicador(fator):
    # Define uma função interna que captura 'fator'
    def multiplicar(numero):
        return numero * fator
    return multiplicar

# Criando closures específicas
dobro = multiplicador(2)  # A closure captura 'fator = 2'
triplo = multiplicador(3)  # A closure captura 'fator = 3'

# Usando as closures
print(dobro(5))  # Saída: 10
print(triplo(5))  # Saída: 1
```

**Funções Lambda:** Em Python, uma função anônima ou lambda é uma função pequena e sem nome, que pode ser definida em uma única linha. Elas são úteis quando você precisa de uma função rápida para ser usada como argumento ou dentro de expressões, mas não quer criar uma função nomeada com def.

- **Lambda Simples:**
    ```Python
    soma = lambda x, y: x + y
    print(soma(3, 5))  # Saída: 8
    ```

- **Usando lambda com map:**
    ```Python
    numeros = [1, 2, 3, 4, 5]
    quadrados = list(map(lambda x: x**2, numeros))
    print(quadrados)  # Saída: [1, 4, 9, 16, 25]
    ```

- **Usando lambda com filter:**
    ```Python
    numeros = [10, 15, 20, 25, 30]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)  # Saída: [10, 20, 30]
    ```

- **Lambda com sorted e chave personalizada:**
    ```Python
    pessoas = [
        {"nome": "Ana", "idade": 25},
        {"nome": "Pedro", "idade": 30},
        {"nome": "Maria", "idade": 22},
    ]
    ordenado = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
    print(ordenado)
    # Saída: [{'nome': 'Maria', 'idade': 22}, {'nome': 'Ana', 'idade': 25}, {'nome': 'Pedro', 'idade': 30}]
    ```

- **Lambda diretamente no código:**
    ```Python
    multiplica = (lambda a, b: a * b)(3, 4)
    print(multiplica)  # Saída: 12
    ```

**Map:** A função map em Python é usada para aplicar uma função a cada item de um iterável (como uma lista, tupla ou string), retornando um iterador com os resultados. É uma forma eficiente e elegante de transformar dados em massa sem usar loops explícitos.

- **Exemplos:**

    ```Python
    numeros = [1, 2, 3, 4, 5]
    resultado = map(lambda x: x * 2, numeros)
    print(list(resultado))  # Saída: [2, 4, 6, 8, 10]
    ```

    ```Python
    celsius = [0, 10, 20, 30]
    fahrenheit = map(lambda x: (x * 9/5) + 32, celsius)
    print(list(fahrenheit))  # Saída: [32.0, 50.0, 68.0, 86.0]
    ```

    ```Python
    def quadrado(x):
    return x ** 2

    numeros = [1, 2, 3, 4]
    resultado = map(quadrado, numeros)
    print(list(resultado))  # Saída: [1, 4, 9, 16]
    ```

    ```Python
    a = [1, 2, 3]
    b = [4, 5, 6]

    soma = map(lambda x, y: x + y, a, b)
    print(list(soma))  # Saída: [5, 7, 9]
    ```

    ```Python
    nomes = ["ana", "pedro", "maria"]
    capitalizados = map(str.capitalize, nomes)
    print(list(capitalizados))  # Saída: ['Ana', 'Pedro', 'Maria']
    ```

**Filter:** A função filter em Python é usada para filtrar elementos de um iterável com base em uma função fornecida. Ela retorna apenas os elementos para os quais a função retornou True.

- **Exemplos:**

    ```Python
    numeros = [1, 2, 3, 4, 5, 6]
    pares = filter(lambda x: x % 2 == 0, numeros)
    print(list(pares))  # Saída: [2, 4, 6]
    ```

    ```Python
    palavras = ["gato", "cachorro", "elefante", "onça"]
    curtas = filter(lambda x: len(x) <= 5, palavras)
    print(list(curtas))  # Saída: ['gato', 'onça']
    ```

    ```Python
    def maior_que_10(x):
    return x > 10

    numeros = [5, 10, 15, 20]
    resultado = filter(maior_que_10, numeros)
    print(list(resultado))  # Saída: [15, 20]
    ```

    ```Python
    dados = [0, 1, None, 2, "", 3]
    nao_nulos = filter(None, dados)
    print(list(nao_nulos))  # Saída: [1, 2, 3]
    # Quando a função passada é None, o filter elimina valores que são considerados falsos em Python (0, None, "", etc.).
    ```

    ```Python
    nomes = ["Ana", "João", "Pedro", "Maria"]
    com_a = filter(lambda nome: 'a' in nome.lower(), nomes)
    print(list(com_a))  # Saída: ['Ana', 'Maria']
    ```

**Reduce:** A função reduce em Python, disponível no módulo functools, é usada para aplicar uma função de maneira cumulativa a todos os elementos de um iterável, reduzindo-o a um único valor.

Diferentemente de map e filter, que processam cada elemento individualmente, reduce combina elementos sequencialmente para produzir um resultado acumulado.

- **Exemplos:**

    ```Python
    from functools import reduce

    numeros = [1, 2, 3, 4, 5]
    soma = reduce(lambda x, y: x + y, numeros)
    print(soma)  # Saída: 15
    ```

    ```Python 
    from functools import reduce

    numeros = [1, 2, 3, 4, 5]
    produto = reduce(lambda x, y: x * y, numeros)
    print(produto)  # Saída: 120
    ```

    ```Python
    from functools import reduce

    numeros = [7, 2, 10, 4]
    maior = reduce(lambda x, y: x if x > y else y, numeros)
    print(maior)  # Saída: 10
    ```

    ```Python
    from functools import reduce

    palavras = ["Python", "é", "muito", "legal"]
    frase = reduce(lambda x, y: x + " " + y, palavras)
    print(frase)  # Saída: "Python é muito legal"
    ```

    ```Python
    from functools import reduce

    numeros = [1, 2, 3]
    soma_com_inicial = reduce(lambda x, y: x + y, numeros, 10)
    print(soma_com_inicial)  # Saída: 16
    ```

**Recursividade:** A recursividade é um conceito em programação onde uma função chama a si mesma para resolver subproblemas menores de um problema maior. É especialmente útil para problemas que podem ser divididos em partes menores, similares ao problema original.

Uma função recursiva geralmente possui duas partes principais:

- **Caso base:** A condição que termina a recursão. Sem isso, a recursão seria infinita e resultaria em um erro.
- **Chamada recursiva:** A parte onde a função chama a si mesma para trabalhar em um subproblema.

- **Exemplos:**

    ```Python
    def fatorial(n):
        if n == 0:  # Caso base
            return 1
        else:
            return n * fatorial(n - 1)  # Chamada recursiva

    print(fatorial(5))  # Saída: 120
    ```

    ```Python
    def fibonacci(n):
        if n == 0:  # Caso base
            return 0
        elif n == 1:  # Caso base
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)  # Chamada recursiva

    print(fibonacci(6))  # Saída: 8
    ```

    ```Python
    def soma_lista(lista):
        if not lista:  # Caso base: lista vazia
            return 0
        else:
            return lista[0] + soma_lista(lista[1:])  # Chamada recursiva

    print(soma_lista([1, 2, 3, 4, 5]))  # Saída: 15
    ```

### **Docker para Desenvolvedores (com Docker Swarm e Kubemetes)**

**O que é Docker?**

É um software que reduz a complexidade de setup de aplicações, onde configuramos containers que ajem como servidores para rodar as aplicações. Com facilidade, pode-se criar ambientes independentes e que funcionam em diversos Sistemas Operacionais. Fora que ele deixa os projetos ***perfomáticos***.

- **Vantagens de utilizar o Docker:**
    - Proporciona mais velocidade na configuração do ambiente de desenvolvimento.
    - Pouco tempo gasto em manutenção, containers são executados como configurados. 
    - Performance para executar aplicações, mais perfomáticas que uma Virtual Machine.