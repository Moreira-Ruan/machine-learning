# Importe a biblioteca Pandas
import pandas as pd

# Carregue um arquivo CSV para um DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Imprima as primeiras 5 linhas do DataFrame
print(df.head())

# Obtenha informações sobre o DataFrame (tipos de dados, etc.)
print(df.info())

# Calcule estatísticas descritivas das colunas numéricas
print(df.describe())