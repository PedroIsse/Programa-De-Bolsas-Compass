# Módulo datetime para que eu possa receber o valor do dia de hoje
from datetime import datetime 

nome = "Pedro"
idade = 19

# Cálculo da data em que faria 100 anos (Dia de Hoje + (100 - Minha Idade)
ano_100 = datetime.now().year + (100 - idade) 

print(ano_100)