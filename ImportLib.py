import pandas as pd
#Carregando o dataset corretamente ==> neste caso, usa o separador ';'
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

#Exibe as 10 primeiras linhas do Dataframe
print(data.head(10))