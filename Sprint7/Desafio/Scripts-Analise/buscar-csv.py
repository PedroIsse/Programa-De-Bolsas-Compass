import pandas as pd

# Arquivos
filmes_txt = "filmes.txt"
movies_csv = "movies.csv"

# Carrega o CSV
df = pd.read_csv(movies_csv, sep="|")

# Converte as colunas de título para um conjunto para busca eficiente
titulos_csv = set(df["tituloPincipal"].dropna()) | set(df["tituloOriginal"].dropna())

# Lê os títulos do TXT e separa corretamente
with open(filmes_txt, "r", encoding="utf-8") as f:
    filmes_lista = f.read().replace("\n", "").split(",")

with open('filmes-no-csv.txt', 'w', encoding="utf-8") as saida:
    # Verifica quais filmes estão no CSV
    for titulo in filmes_lista:
        titulo = titulo.strip()  # Remove espaços em branco extras
        if titulo in titulos_csv:
            saida.write(f"O filme '{titulo}' está no CSV!\n")
        else:
            saida.write(f"O filme '{titulo}' NÃO está no CSV!\n")
