import pandas as pd

df = pd.read_excel('SeguradorasNormalização 1.xls', dtype=str)

df['DIA'] = df['Data'].str.strip().str.split().str[1].astype(str)

df.to_excel("SeguradorasNormalização 1.xlsx", index=False)