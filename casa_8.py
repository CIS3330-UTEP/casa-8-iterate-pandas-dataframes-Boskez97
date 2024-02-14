import pandas as pd

data = {'name': ['Mexico','Poland'],
        'currency_code': ['MXN', 'PLN']}

df = pd.read_csv('big-mac-full-index.csv')
#iterrows method:
for i,r in df.iterrows():
    print(r['name'], r['currency_code'])
#apply method:
print(df.apply(lambda row: row["name"] + ' ' + str(row['currency_code']), axis =1))
