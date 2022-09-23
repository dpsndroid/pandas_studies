import pandas as pd


dados = pd.read_excel("tecnico.xlsx")
dados.head()
print(dados)
print("----------------------------------")

# selecionando uma coluna por índice
print(dados["nome"].head())
print("----------------------------------")
# selecionando várias colunas por índice
print(dados[["nome", "telefone"]])
print("----------------------------------")
dados["ficha"] = dados["nome"] + " " + dados["turno"]
print(dados.head())
print("---------------------------------------")