import pandas as pd

df = pd.read_excel('SeguradorasNormalização 1.xls', dtype=str)
df.to_excel("SeguradorasNormalização 1.xlsx", index=False)