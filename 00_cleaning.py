import pandas as pd

files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

dfs = []
for file in files:
    dfs.append(pd.read_csv('data/' + file))

df = pd.concat(dfs)
df['price'] = df['price'].apply(lambda x: x[1:]).astype(float)
df['sales'] = df['quantity'] * df['price']
subset = df[df['product'] == 'pink morsel']

subset[['sales', 'date', 'region']].to_csv('./data/pink_morsel_sales.csv')
