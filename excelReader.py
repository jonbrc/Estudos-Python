import pandas as pd

# Ler a planilha
planilha = pd.read_excel("C:/Users/jbrca/Downloads/planilha.xlsx")

# Imprimir uma coluna
print(planilha["Unnamed: 4"])