import pandas as pd


def linha():
    print("----------------------------------------------")


dados = pd.read_excel("tecnico.xlsx")
dados.head()
print(dados)
linha()

# Usando o Loc

print(dados.loc[2])
linha()
print(dados.loc[2:4])
linha()
print(dados.loc[[0,2,4]])
linha()
print(dados.loc[2:4, "nome"])
linha()
print(dados.loc[2:4, ["nome", "turno"]])
linha()
print(dados.loc[2:4, "cpf" : "telefone"])
linha()
linha()
print(dados.iloc[2])
linha()
print(dados.iloc[2:4]) # iloc não irá incluir o último número
linha()
print(dados.iloc[[0,2,4]])
linha()
print(dados.iloc[2:4, 3]) # iloc não retorna nome, só número de linha e coluna
linha()
print(dados.iloc[2:4, 1:4])
linha()
print(dados.iloc[[2,4], [True, True, True, True, True]])
linha()
print(dados.iloc[[2,4], [False, True, False, True, True]])
linha()