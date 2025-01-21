# **Resolução: TMDB**

### **Entendimento:** 

Uma vez que utilizaremos a API do TMDB para coletar dados para a análise final do desafio, é importe que tenhamos uma ideia de como a API funciona. Então para isso iremos fazer um *request* para a API com o título, data de lançamento, visão geral, votos e média de votos dos ***filmes*** que estão presentes no banco de dados do tmdb.

[**Script Utilizado:**](./conexao-api.py)

```Python
import requests
import pandas as pd
from IPython.display import display
import os
from dotenv import load_dotenv

# Carrega a variável de ambiente do arquivo .env (API Key)
load_dotenv()

api_key = os.getenv('api_key')

url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR'

response = requests.get(url)

data = response.json()
filmes = []

for movie in data['results']:
    df = {
        'Titulo': movie['title'],
        'Data de Lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(df)

# Cria o DataFrame
df = pd.DataFrame(filmes)
display(df)
```

**Resultado de execução:**

![Resultado de Execução](../../../Sprint7/Exercicios/Imagens/conexao-api-sucesso.png)