import pandas as pd

df = pd.read_csv("teste.csv", encoding= "utf-8", sep=",", header=0, usecols=["Terceiro"], nrows=3)
# header escolhe a linha que inicia e ignora o que estiver acima
df.head()
print("-------------------")
print(df)
print("-------------------")
