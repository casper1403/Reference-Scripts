import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 500)
df = pd.read_csv('obisityData.csv')
print(df)

# .1 is male .2 is female
