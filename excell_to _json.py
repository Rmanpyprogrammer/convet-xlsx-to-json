import pandas as pd

with pd.ExcelFile("1.xlsx") as x:
    df=pd.read_excel(x)
    
df.to_json('output.json', orient='records')

