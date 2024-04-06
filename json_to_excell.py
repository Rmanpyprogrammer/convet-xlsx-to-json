import pandas as pd

with open('backup_1.json', 'r') as f:
    data = f.read()

df = pd.read_json(data)


with pd.ExcelWriter("1.xlsx",mode="a",if_sheet_exists="replace") as writer:
    df.to_excel(writer,sheet_name="1",index=False)