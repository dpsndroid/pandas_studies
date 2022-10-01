import pandas as pd


def linha():
    print("----------------------------------------------")


titanic = pd.read_csv("titanic.csv")
titanic.head()
print(titanic)
linha()

print(titanic["Name"].str.lower()) # converte para minúsculo na seleção
linha()

print(titanic["Name"].str.split(",")) # cria uma lista com 2 itens dividido a partir da vírgula
linha()

titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)

print(titanic["Surname"])
linha()

print(titanic["Name"].str.contains("Countess"))
linha()

print(titanic[titanic["Name"].str.contains("Countess")])
linha()

print(titanic["Name"].str.len()) # nome com o maior comprimento
linha()

print(titanic["Name"].str.len().idxmax())
linha()

print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])
linha()

titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
print(titanic["Sex_short"])
linha()

