import pandas as pd

df = pd.read_excel("tecnico.xlsx", sheet_name=1)
arquivo = pd.ExcelFile("tecnico.xlsx")
df.head()
aba1 = arquivo.parse("Testing")
aba2 = arquivo.parse("Planilha1")
print("-------------------")
print(df)
print("-------------------")
print(df.shape)
print(arquivo.sheet_names)
print(aba1)
print("--------------------")
print(aba2)
print("--------------------")

