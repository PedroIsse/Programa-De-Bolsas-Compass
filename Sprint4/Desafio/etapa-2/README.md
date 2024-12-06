### **ETAPA 2 - DESAFIO SPRINT 02**

**Pergunta:** *É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.*

Sim, é possível reiniciar um container já utilizado. Vamos usar a [***etapa 1***](../etapa-1/) como exemplo. O arquivo [***carguru.py***](../etapa-1/carguru.py) possui uma lista com 56 carros, e o objetivo do algoritmo é escolher aleatoriamente um dos carros na lista e imprimir no terminal do usuário, uma atividade ***instantânea*** ela irá escolher um carro e acabou seu uso, para isso usamos o comando:

```
docker run resolucao-etapa-1
```

O container será executado e armazenado numa espécie de *"histórico"* que pode ser acessado por:

```
docker ps -a
```

Esse comando permite visualizar os containers que estão executando e aqueles que já foram executados, podemos dizer que ali é quase como uma lista de espera, pois podemos chamar o container novamente para executar, **quantas vezes acharmos que for necessário**, usando esse comando:

```
docker start <id do container>
```

Isso fará com que ele seja executado, novamente, mas como sua execução é instantânea para verificarmos às ações do container usamos o comando:

```
docker logs <id do container>
```

Nele serão exibas às ocorrências durante a execução do container, no contexto da [***etapa 1***](../etapa-1/) será mostrado a seguinte mensagem:

```
Você deve dirigir um <carro presente na lista>
```

Podendo ser o mesmo carro ou um carro diferente, ou até mesmo, algum erro durante a execução do container.