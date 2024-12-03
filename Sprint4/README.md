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
    - Proporciona mais velocidade na configuração do ambiente de desenvolvimento
    - Pouco tempo gasto em manutenção, containers são executados como configurados
    - Performance para executar aplicações, mais perfomáticas que uma Virtual Machine

**Trabalhando com Containers:** Um pacote de código que pode executar uma ação, por exemplo: rodar uma aplicação Python. Ou seja, os projetos serão executados dentro de containers que criarmos/utilizarmos.

- Containers utilizam **imagens** para poderem ser executados 

- Múltiplos containers podem rodar juntos, exemplo: um para PHP e outro para MySQL.

**Container X Imagem:**

- São recursos **FUNDAMENTAIS** do Dccker
- Imagem é o **projeto** que será executado pelo container, todas as instruções estarão declaradas nela
- Container é o **Docker executando alguma imagem**, consequentemente executando algum código proposto por ela
- O fluxe é: Programamos uma imagem e a executamos por meio de um container

**Rodando um Container:**

- Imagens podem ser encontradas em: https://hub.docker.com

- Executando uma imagem com o comando:
    ```Docker
    docker pull <image>
    docker run <image>
    ```

**Verificar containers executados:**

- Os comandos:

    ```Docker
    docker ps 

    docker ls
    ```
    
    Exibem quais containers estão sendo executados no momento

- Utilizando a flag -a, temos também **TODOS** os containers já executados na máquina

- Estes comando são úteis para entender o que está sendo executado e acontece no nosso ambiente de trabalho

**Rodando containers no modo iterativo:**

- Podemos rodar um container e deixá-lo executando no terminal 

- Desta maneira, pode-se executar comandos disponíveis no container que está sendo utilizado pelo comando run

```Docker
docker pull ubuntu
docker run -it ubuntu # Irá abrir o terminal do Ubuntu
```

**Container X Virtual Machine:** 

- Container é uma aplicação que serve para um determinado fim, não possui sistema operacional, seu tamanho são alguns MBs

- Virtual Machines possuem sistemas Operacionais próprio, tamanho de GBs, pode executar diversas funções ao mesmo tempo

- Containers gastam menos recursos ao serem executados, enquanto VMs gastam mais recursos, pois elas podem exercer mais funções

**Executando container em background:** 

- Quando iniciamos um container que persiste, ele fica ocupando o terminal, podemos então executar o container em background para que não fiquem muitas abas de terminal abertas 

    ```Docker
    docker pull <image>
    docker run -d <image>
    ```

**Exportar portas:** 

- Os containers de Docker **NÃO TEM CONEXÃO COM NADA FORA DELES**

- Por conta disso, exportamos portas:

```Docker
docker run -d -p 80:80 nginx 

docker stop <id ou nome> # Para a execução de um container específico

# PRIMEIRA PORTA - EXPONDO NO PC 
# SEGUNDA PORTA - RECEBER DO CONTEINER 
```

**Reiniciando Containers:** O *docker run* **SEMPRE** cria um novo container, por isso em caso de necessidade usar:

```Docker 
docker start <id>

# Volta com as configurações e alterações JÁ SETADAS
```

**Definindo nome de container:** Os nomes iniciais dos containers são aleatórios e pouco profissionais, para isso existe um comando para alterar o nome:

```Docker
docker pull <image>
docker run --name <nome> <image>
```

**Verificando Logs:** Podemos verificar o que aconteceu com um container com o comando:

```Docker
docker logs <id>

# As últimas ações realizadas, serão exibidas no terminal
```

**Removendo container:**

```Docker
docker rm <id> # Remove um container

docker rm <id> -f # Força um container que está em execução a ser removido

docker run --rm <container> # Remove automaticamente o container após sua utilização, dessa forma economizamos espaço na máquina
```

**O que é uma imagem?** 

Imagens são originadas de arquivos que programamos para que o Docker crie uma estrutura que execute determinadas ações em containers. Elas contém informações como: imagens base, diretório base, comandos a serem executados, porta da aplicações.

Ao rodar um container baseado na imagem, as instruções serão executadas em camadas. 

**Criando imagens:**

- Para criar uma imagem é necessário um arquivo **Dockerfile** em uma pasta que ficará o projeto.

- Instruções neste arquivo:
    - **FROM:** Imagem base
    - **WORKDIR:** Diretório de aplicação
    - **EXPOSE:** Porta de aplicação
    - **COPY:** Quais arquivos precisam ser copiados
    - **CMD**

    ```Docker
    FROM python:3.11.4-slim

    WORKDIR /app

    COPY app.py .

    EXPOSE 8000

    CMD ["python", "app.py"]
    ```

**Excutando uma imagem:** 

- Para executar uma imagem primeiramente vamos fazer o build:

    ```Docker
    docker build <diretório da imagem>

    docker run <imagem>
    ```

**Alterando uma imagem:** Sempre que for alterado o código da imagem, será necessário fazer o build novament, pois para o Docker é como se fosse uma imagem **completamente nova**.

**Camadas/Cache/Layers das imagens:** As imagens são divididas em camadas, cada instrução do Dockerfile representa uma camada. Quando algo é atualizado apenas as camadas **DEPOIS** da linha atualizada são refeitas o resto permanece em cache, tornando o build mais rápido.

**Múltiplas aplicações, mesmo container:** Podemos inicializar vários containers com a mesma imagem, as aplicações funcionarão em paralelo.

**Nomeando imagens:**

```Docker
docker tag <imagem> <nome>

docker tag <imagem> <nome>:<tag>

# Pode nomear a tag NO COMANDO BUILD

docker build -t <nome> .

docker build -t <nome>:<tag> .
```

**Removendo Imagens:**

```Docker
docker rmi <nome ou id>

docker rmi <nome ou id> -f # Força a remoção
```
**Removendo imagens, containers e networks não utilizados:**

```Docker
docker system prune # O sistema irá exigir uma confirmação para realizar a remoção
```

**Copiando arquivos entre containers:** Podemos utilizar para copiar um arquivo de um diretório para um container ou de um container para um diretório. 

```Docker
docker cp 
```

**Comandos de análise de containers:**

- **Verificar informações de processamento:** Temos acesso a quando ele foi iniciado , id do processo, descrição do comando CMD

    ```Docker
    docker top <container>
    ```

- **Verificar dados de um container:** Verifica diversas informações, como: id, data de criação, imagem, entre outros.

    ```Docker
    docker inspect <container>
    ```

- **Verificar processamento:** Os processos que estão sendo executados em um container, desta forma temos acesso ao andamento do processamento e da memória gasta:

    ```Docker
    docker stats
    ```

**Enviar as próprias imagens para o Docker Hub:** 

- **Criar conta no site do Docker Hub**
- **Autenticar no terminal com:**
    ```Docker
    docker login 
    # <user> 
    # <password>

    docker logout # Encerra a sessão com o Docker Hub
    ```
- **Enviar a imagem:**

    ```Docker
    docker push <imagem>

    # Lembrando que a imagem deve ter o mesmo nome do repositório:

    # pedroisse/testecursodocker

    # Para atualizações na imagem, mudar sua TAG (Versionamento de código)
    ```

**Introduzindo volumes aos containers:**

**O que são volumes?**

Uma forma prática de persistir dados em aplicações e não depender de containers para isso. Todo dado criado por um container é salvo nele, quando o container é removido, os dados também são. Por conta disso, precisamos dos volumes para gerenciar os dados e também conseguir fazer backups de forma mais simples.

**Tipos de volumes:**

- **Anônimos (anonymous):** Diretórios criados pela ***flag -v***, porém com um nome aleatório

    ```Docker
    docker volume create 

    # Volumes anônimos são criados automaticamente quando não especifica um nome, e o Docker os gerencia automaticamente

    docker run -d -v /caminho/no/container nome_da_imagem
    ```

- **Nomeados (named):** São volumes com nomes, podemos nos referir a estes facilmente e saber para que são utilizados no nosso ambiente

    ```Docker
    docker volume create nome_do_volume

    # Volumes nomeados são volumes explícitos com um nome fornecido pelo usuário. O Docker gerencia seu ciclo de vida.

    docker run -d -v nome_do_volume:/caminho/no/container nome_da_imagem
    ```

- **Bind mounts:** Uma forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informamos um diretório para esse fim

    ```Docker
    # Bind mounts são volumes que referenciam arquivos ou diretórios específicos do host. Eles podem ser usados para persistência de dados de forma mais flexível, vinculando uma pasta no host com uma no contêiner.

    docker run -d -v /caminho/no/host:/caminho/no/container nome_da_imagem
    ```

    Bind Mounts também serve para atualizações em tempo real do projeto, ou seja, sem ter que refazer o build a cada atualização do mesmo.

**Manipulação de Volumes:**

- **Inspecionar Volumes:** Sua função é permitir o acesso ao local em que o volume guarda dados, nome, escopo e muito mais. O Docker salva os dados dos volumes em algum diretório do nosso computador, desta forma podendo saber qual é.

    ```Docker
    docker volume inspect <nome>
    ```

- **Removendo Volumes:**

    ```Docker
    docker volume rm <nome>

    # Remove um volume, simples, mas TODOS OS DADOS também serão removidos

    docker volume prune

    # Remove TODOS os volumes que não estão sendo utilizados, e novamente, TODOS OS DADOS também serão removidos
    ```

- **Volumes somente leitura:** 

    ```Docker
    docker run -d -v /caminho/no/container:ro nome_da_imagem

    # ro = Read Only
    ```

**Conectando containers com Networks:**

**O que são Networks?**

São uma forma de gerenciar a conexão do Docker com outras plataformas ou até mesmo containers. As redes ou networks são criadas separadas do containers, tal qual o volume.

**Tipos de Conexão:**

- **Externa:** Conexão com uma API de servidor remoto 

- **Com o host:** Comunicação com a máquina que está executando o Docker

- **Entre containers:** Comunicação que utiliza o driver bridge e permite a comunicação entre dois ou mais containers

**Tipos de Drivers:** 

- **bridge:** O mais comum e default do Docker, utilizado quando containers precisam se conectar (na maioria das vezes optamos por este driver)

- **host:** permite a conexão entre um container e a máquina que está hosteando o Docker

- **macvlan:** permite a conexão do container por um MAC address

- **none:** remove todas as conexões de rede de um container

- **plugins:** permite extensões de terceiros para criar outras redes

**Comandos de Redes:**

- **Listando Networks:**

    ```Docker
    docker network ls

    # Algumas redes já estão criadas, pois fazem parte da configuração inicial do Docker
    ```

- **Criando Redes:**

    ```Docker
    docker network create <nome>

    # Por padrão o driver da rede será do tipo bridge

    docker network create -d <tipo de driver> <nome>

    # Para escolher o tipo de driver específico utiliza a flag -d e o tipo de driver
    ```

- **Removendo Redes:** 

    ```Docker
    docker network rm <nome>

    # Remove uma rede específica

    docker network prune

    # Remove todas as redes que não estão sendo utilizadas
    ```

- **Conectando e desconectando um container a uma rede:** 

    ```Docker
    docker network connect <rede> <container>

    docker network disconnect <rede> <container>
    ```

- **Inspecionando Redes:** 

    ```Docker
    docker network inspect <rede>
    ```

**Introdução ao YAML:**

**O que é YAML?**

É uma linguagem de serialização, seu nome é **YAML ain't Markup Language**. Usada geralmente para arquivos de configuração, inclusive do Docker, para configurar o Docker Compose. É de fácil leitura e sua extensão é yml ou yaml.

**Criando um arquivo YAML:** O arquivo .yaml geralmente possui chaves e valores, que é onde vamos retirar as configurações do nosso sistema. Para definir uma chave apenas inserimos nome dela, em seguida colocamos dois pontos e depois o valor.

O fim de uma linha indica o fim de uma instrução, não há ponto e vírgula, a identenção **deve conter um ou mais espaços** e não devesse utilizar o tab, e cada linha define um novo bloco. O espaço é **obrigatório após a declaração da chave**.

**Tipos de dados:**

- **Númericos:**
    - **INT:** 3
    - **FLOAT:** 3.14

- **Strings:**
    - **Com aspas:** "Digite um texto" ou 'Digite um texto'
    - **Sem aspas:**  Digite um texto

- **Dados nulos:** 
    - **~**
    - **null**

- **Booleanos:**
    - **True e On:** VERDADEIRO
    - **False e Off:** FALSO

- **Listas ou Arrays:**
    - **Horizontal:** [1, 2, 3, 4]
    - **Vertical:**:
        - items:
            - \- 1
            - \- 2
            - \- 3

- **Dicionários ou Objetos:**
    - **Horiziontal:** obj: {a: 1, b: 2, c: 3}
    - **Vertical:**
        - obj:
            - chave: 1
            - chave: 2
            - chave: 3

**Gerenciamento múltiplos containers com Docker Compose:** 

**O que é Docker Compose?**

O Docker Compose é uma ferramenta para rodar múltiplos containers, teremos apenas um arquivo de configuração, que orquestra totalmente esta situação. É uma forma de rodar múltiplos builds e runs com um comando. **Em projetos maiores é essencial o uso do Compose.**

**Exemplo de como pode ser um arquivo Docker-Compose:**

```YAML 
version: '3.9'

services:
  web:
    image: python:3.11
    container_name: web-app
    working_dir: /app
    volumes:
      - ./app:/app
    ports:
      - "5000:5000"
    command: >
      sh -c "
      pip install -r requirements.txt &&
      python app.py"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase
    depends_on:
      - db

  db:
    image: postgres:15
    container_name: postgres-db
    restart: always
    volumes:
      - db_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"

volumes:
  db_data:
```

**Como rodar um Compose:**

```Docker
docker-compose up 

# Isso fará com que as instruções do arquivo sejam executadas

docker-compose up -d 

# Isso fará com que as instruções do arquivo sejam executadas em background

docker-compose down # Para a execução do Compose
```

**Variáveis de ambiente:** Podemos definir variáveis de ambiente para o Docker Compose. Para isso vamos definir um arquivo base em **env_file**, as variáveis podem ser chamadas pela sintaxe **${variável}**. É útil quando o dado a ser inserido é sensível/não pode ser compartilhado, como uma senha. 

**Exemplo:**

```YAML
version: '3.9'

services:
  web:
    image: python:3.11
    container_name: web-app
    working_dir: /app
    volumes:
      - ./app:/app
    ports:
      - "5000:5000"
    command: >
      sh -c "
      pip install -r requirements.txt &&
      python app.py"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase
    depends_on:
      - db

  db:
    image: postgres:15
    container_name: postgres-db
    restart: always
    volumes:
      - db_data:/var/lib/postgresql/data
    env_file:
        - ./testecompose/db.env
    ports:
      - "5432:5432"

volumes:
  db_data:
```

**Arquivo db.env:**

```Enviroment
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=mydatabase
```

**Redes no Compose:** O compose cria uma rede básica Bridge entre os containers da aplicação, porém podemos isolar as redes com a chave **networks**, desta maneira, podemos conectar apenas os containers que optarmos. Também podemos definir drivers diferentes. 

**Docker Swarm para orquestração:**

**O que é orquestração de containers?**

É o ato de conseguir **gerenciar e escalar** os containers da nossa aplicação, temos um serviço que rege sobre outros serviços, verificando se os mesmos estão funcionando como deveriam. Desta forma, conseguimos garantir uma aplicação saudável e também que esteja sempre disponível. Alguns serviços:

- **Docker Swarm**
- **Kubernetes**
- **Apache Mesos**

**O que é Docker Swarm?**

Uma ferramenta do Docker para orquestrar containers, podendo escalar horizontalmente nossos projetos de maneiras mais simples, o famoso **cluster**. A facilidade do Swarm para outros orquestradores é que todos os comandos são muito semelhantes ao do Docker. 

***Toda instalação do Docker já vem com Swarm, porém desabilitado***

**Conceitos Fundamentais do Swarm:**

- **Nodes:** É uma instância (máquina) que participa do Swarm

- **Manager Node:** Node que gerencia os demais Nodes

- **Worker Node:** Nodes que trabalham em função do Manager

- **Service:** Um conjunto de Tasks que o Manager Node manda o Work Node executar

- **Task:** Comandos que são executados nos Nodes

**Docker Swarm com AWS:**

- **AWS Services:**

    - **EC2** (Máquinas (Instâncias) utilizadas para rodar projetos webs)

        - Selecionar a imagem: ***AMAZON LINUX***

**Comandos Utilizados no Swarm:**

- **Inicializando Swarm:** 
    ```Docker
    docker swarm init 

    # Ou 

    docker swarm init --advertise-addr <ip do servidor>

    # Isso fará com que a instância/máquina vire um Node, e também transforma em um Manager
    ```

- **Listando Nodes Ativos:**

    ```Docker
    docker node ls

    # Permite monitorar o que o Swarm está monitorando
    ```

- **Adcionando Instâncias ou Novos Nodes:**

    ```Docker
    docker swarm join --token <token> <ip>:<porta>

    # Em AWS é NECESSÁRIO instalar o Docker em cada instância antes disso

    # Normalmente essa linha de código é fornecida quando você inicia o Manager Node

    # Dessa maneira são conectadas duas instâncias
    # A novo instância entra como WORKER todas as TASKS utilizadas na Manager, serão aplicadas em Nodes que foram aplicados com join (workers)

    docker swarm join-token manager

    # Recupera o TOKEN do manager sem que tenha que sair do SWARM e consequentemente, bagunçar toda a estrutura já criada
    ```

- **Subindo um novo serviço:**

    ```Docker
    docker service create --name <nome> <imagem>

    # Desta forma teremos um container novo sendo adicionado ao Manager
    # Esta serviço será gerenciado pelo Swarm

    docker service ls

    # Para listar todos os serviços em execução, tal qual algumas de suas informações (nome, replicas, imagem, porta)

    docker service rm <serviço>

    # O serviço para de rodar, ou seja, o container que está rodando e outras consequências devido a parada do mesmo
    ```

- **Replicando serviços:**

    ```Docker
    docker service create --name <nome> --replicas <numero><imagem>

    # Desta maneira uma task será emitida, replicando este serviço nos Workers
    # Assim, finalmente, iniciando a orquestração   

    # Caso algum serviço dos WORKERS CAIA OU SEJA REMOVIDO DURANTE SUA OPERAÇÃO O SWARM IRÁ REINCIAR O CONTAINER RAPIDAMENTE
    ```

- **Inspecionando Serviços:**

    ```Docker
    docker service inspect <ID>

    # Receberemos informações como: nome, data de criação, portas e etc
    ```

- **Checando as informações do Swarm:**

    ```Docker
    docker info

    # Podemos visualizar o ID do Node, número de Nodes, número de Managers Nodes e mais!
    ```

- **Removendo uma Instância do Swarm:**

    ```Docker
    docker swarm leave

    docker swarm leave --force
    
    # A instância deixa de ser contada mais como um Node para o Swarm
    ```

- **Removendo um Node:** 

    ```Docker
    docker node rm <id>

    docker node rm <id> -f 
    ```

- **Verificar quais containers ativados pelo service:**

    ```Docker 
    docker service ps <id da imagem>

    # Receberemos uma lista de containers que estão rodando e também dos que já receberam baixa
    ```

- **Compose no Swarm:**

    ```Docker
    docker stack deploy -c <arquivo.yaml> <nome>
    
    # Assim podemos utilizar um compose em Docker Swarm, mas não faz muito sentido, pois no Swarm podemos utilizar réplicas
    ```

- **Aumentando réplicas do Stack:**

    ```Docker
    docker service scale <nome>=<replicas>

    # Desta forma as outras instâncias receberão as TASKS a serem executadas
    ```

- **Fazer um serviço não receber mais Tasks:**

    ```Docker
    # Fazemos com que o serviço não receba mais ordens do Manager

    docker node update --availbility drain <id>

    # Fazemos com que o serviço volte a receber ordens do Manager

    docker node update --availbility active <id>

- **Atualizar parâmetros de um Serviço:**

    ```Docker
    docker service update --image <imagem> <serviço>

    # O exemplo acima é de uma imagem, mas podem ser outros parâmetros

    # TODOS os Nodes com status ACTIVE irão receber atualizações
    ```

- **Criando rede para Swarm:**

    ```Docker
    # As instâncias usam um driver diferente o OVERLAY

    docker network create

    # Ao criar um service adicionar flag --network <rede> para inserir as instâncias na nossa nova rede

    docker network crate --driver overlay swarm

    #  Podemos também conectar serviços que já estão em execução a uma rede

    docker service update --network-add <rede> <nome>
    ```

**Orquestração com Kubernetes:**

**O que é Kubernetes?**

Uma ferramente de orquestração, permite criação de múltiplos containers em diferentes máquinas (nodes). Escalando projetos, formando um cluster. Gerencia serviços, garantindo que as aplicacações sejam executadas sempre da mesma forma. Criada pela Google.

**Conceitos fundamentais:**

- **Control Plane:** Onde é gerenciado o controle dos processos dos Nodes

- **Nodes:** Máquinas que são gerenciadas pelo Control Plane

- **Deployment:** A execução de uma imagem/projeto em um Pod

- **Pod:** Um ou mais containers que estão em um Node

- **Services:** Serviços que expõe os Pods ao mundo externo

- **kubectl:** Cliente de linha de comando para o Kubernetes

**Inicializando e parando o Minikube:**

```Docker
minikube start --driver=<driver>

# Onde o driver pode ser algum desses: Virtual Box (VMs), Hyper V, Docker

# Podemos testar com:

minikube status

# Para pararmos o minikube:

minikube stop 
```

**Acessando o dashboard do Kubernetes:** O minikube nos disponibiliza um dashboard, nele podemos ver todo o detalhamento de nosso projeto: serviços, pods e etc.

```Docker
minikube dashboard

# Para apenas obeter a URL:

minikube dashboard --url
```

**Deployment:** É uma parte fundamental do Kubernetes, com ele criamos nossos serviços que vão rodar nos pods. Definimos uma imagem e um nome, para posteriormente ser replicado entre os servidores. A partir da criação do deployment teremos containers rodando. 

```Docker
# Assim, o projeto estará sendo orquestrado pelo

kubectl create deployment <nome> --image=<imagem> 

# Assim verificamos o deployment

kubectl get deployments 

# Verificamos o deployment de forma mais detalhada, desta forma 

kubectl describe deployments

# Deletando deployments

kubectl delete deployment <deployment>
```

**Verficando Pods:** Pods são componentes muito importantes também, onde os containers realmente são executados

```Docker
# Assim verificamos os pods

kubectl get pods

# Verificamos os pods de forma mais detalhada, desta forma:

kubectl describe pods
```

**Configurações do Kubernetes:** 

```Docker
kubectl config view
```

**Services:** As aplicações Kubernetes **não tem conexão com o mundo externo**, por conta disso, precisamos criar um Service, que é o que possibilita expor os Pods. Isso acontece pois os Pods são criados para serem destruídos e perderem tudo, ou seja, os dados gerados neles também são apagados. Concluíndo, o Service é uma entidade separada dos Pods, que expõe eles a uma rede.

```Docker
# Criando um serviço:

# Normalmente o tipo usado é o LoadBalancer

kubeclt expose deployment <deployment> --type=<tipo> --port=<port>

# Detalhes do serviço:

kubectl get services

kubectl describe services/<service>

# Deletando serviços:

kubectl delete services <serviço>
```

***Gerando IP de acesso:***

```Docker
minikube service <nome>

# O IP aparece no terminal e abre uma aba no seu navegador
```

***Replicando nossa aplicação:***

```Docker
kubectl scale deployment/<deployments> --replicas=<numero de replicas>

# Verificar no Dashboard do minikube ou com o comando:

kubectl get pods

# Verificar o número de réplicas:

kubectl get rs

# Reduzindo o número de réplicas/diminuir escala

kubectl scale deployment/<deployment> --replicas=<numero menor que o atual>
```

**Atualizando a Imagem do projeto:** A nova imagem deve ser subida no Docker Hub para que seja possível a atualização, tal qual o nome do container.

```Docker
kubectl set image deployment/<deployment> <container>=<nova_imagem>
```

**Desfazendo Alteração no Projeto:** Para fazer uma alteração utilizamos uma ação conhecida como **rollback**.

```Docker
# Verificar alteração:

kubectl rollout status deployment/<deployment>

# Voltar alteração:

kubectl rollout undo deployment/<deployment>
```

**Modo Declarativo com Kubernetes:** O modo declarativo é guiado por um arquivo, semelhante ao Docker Compose. Desta maneira tornamos nossas configurações mais simples e centralizamos tudo em um comando. Também é utilizado um arquivo escrito em **YAML**.

- **Chaves mais utilizadas:**
    - **apiVersion:** versão utilizada da ferramenta
    - **kind:** tipo do arquivo (Deployment, Service)
    - **metadata:** descrever algum objeto, inserindo chaves como name
    - **replicas:** número de replicas de Nodes/Pods
    - **containers:** definir as especificações de containers como: nome e imagem

- **Executando arquivo de Deployment:**
    ```Docker
    # Aplicando o arquivo.yaml

    kubectl apply -f <arquivo.yaml>

    # Parando o deployment

    kubectl delete -f <arquivo.yaml>

    # O Service PRECISA de um arquivo.yaml para si só

    kubectl apply -f <service.yaml>
    minikube service <id> # Acesso

    # Parando serviço:

    kubectl delete -f <service.yaml>
    ```