import pandas as pd
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
print(df)

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
print(df2)

df3 = df.append(df2, ignore_index=False)
print(df3)