import pandas as pd


def linha():
    print("----------------------------------------------")


dados = pd.read_excel("tecnico.xlsx")

print(dados.sort_values("nome").head()) # vai ordenar por nome
linha()

print(dados.head(n=3)) # vai exibir apenas os 3 primeiros
linha()

print(dados.sort_values("equipe").head()) #vai ordenar por equipe
linha()

print(dados.sort_values("equipe").head(n=3)) # ordenar por equipe exibe apenas 3
linha()

print(dados.sort_values(["nome", "turno"]).head()) #ordena por nome e turno
linha()

print(dados.sort_values("nome", ascending=False).head()) #ordena nome de baixo p cima
linha()



