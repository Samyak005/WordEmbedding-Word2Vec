import pandas as pd
import numpy as np
df = pd.read_json (r'recipes.json')
del df['sodium']
del df['fat']
del df['date']
del df['calories']
del df['desc']
del df['protein']
del df['rating']
print(df)
# df = df[:200]

df.to_csv(r'array.txt', header=None, index=None, sep=',', mode='w')
# print(df)
# arr = df.to_numpy()
# print(arr)

# pd.DataFrame(arr).to_csv("recipes.csv", header=None, index=None)