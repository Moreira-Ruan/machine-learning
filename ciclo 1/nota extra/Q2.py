import pandas as pd
import numpy as np

df = pd.DataFrame({ 'A': [10, np.nan, 30, 40, np.nan], 'B': ['X', 'Y', 'X', 'Y', 'X'], 'C': [1.5, 2.5, np.nan, 4.5, 5.5]})

print(df)

df['A'].fillna(df['A'].mean()) #Remover inplace=True

df['C'] = df['C'].interpolate()

df = pd.get_dummies(df, columns=['B'])

print(df)