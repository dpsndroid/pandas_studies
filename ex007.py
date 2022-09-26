import pandas as pd


def linha():
    print("----------------------------------------------")


dados = pd.read_excel("tecnico.xlsx")

print(dados.filter(items= ["cpf", "turno"]).head())
linha()

print(dados.filter(like= "n").head()) # vai exibir os cabeçalhos contendo n
linha()

print(dados.filter(regex=".e.")) #retorna que tenha letra e com algo antes e depois
linha()

print(dados.filter(regex=".e")) # retorna só que não tem nada depois de e
linha()

print(dados.filter(regex=".om."))
linha()

