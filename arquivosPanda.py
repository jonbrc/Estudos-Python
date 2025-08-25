# Pandas é uma biblioteca que permite a operação em larga quantidade de dados através de um
# objeto chamado DataFrame (df)
import pandas as pd

# Através de seus métodos é possível realizar operações em arquivos de forma menos verbosa
df = pd.read_csv("arquivos/filmes.csv")
print(df.head()) # O método head traz as 5 primeiras linhas, pode receber por parâmetro uma quantidade específica

# Outro exemplo, trazer todos os filmes cujo diretor é "Christopher Nolan"
nolan = df[df["diretor"] == "Christopher Nolan"] # Essa primeira estrutura traz uma Series, uma serialização da coluna com booleanos indicando se os valores atendem ou não nossa condição. O df externo cria um dataFrame com os valores positivos
print(nolan)

# Filmes por estúdio, por diretor e por ano
print(df["estudio"].value_counts())
print(df["diretor"].value_counts())
print(df["ano"].value_counts())
# value_counts é um método de Series que conta quantas vezes cada valor aparece na coluna.
# ele retorna outra Series ordenada do mais frequente para o menos frequente.

# Segundo essa lógica para imprimir os filmes que lançaram depois de 2002: 
filmesApos2002 = df[df["ano"] >= 2002]
print(filmesApos2002)

# Aplicando uma lógica de filtragem:
ficcao = df[df["genero"] == "Ficção Científica"]
print(ficcao[["titulo", "ano", "nota_imdb"]])

# Além disso é possível realizar operações matemáticas com valores do csv
mediaNolan = df[df["diretor"] == "Christopher Nolan"]["nota_imdb"].mean() 
# Destrinchando essa estrutura:
# [df["diretor"] == "Christopher Nolan"] - Aplica uma selação de colunas (series) transformando-as em true ou false em função da condição
# ["nota_imdb"] - Limita, do df resultado (colunas true) 
# mean() - Método do pandas que retorna a média de uma série de valores
print(mediaNolan)

# Somatório dos prêmios de Quentin Tarantino
duracaoFilmesTarantino = df[df["diretor"] == "Quentin Tarantino"]["duracao_min"].sum() # O método sum faz uma soma dos valors da coluna
print(duracaoFilmesTarantino)

# Somátorio dos prêmios de steven Spilberg
df["premios_num"] = df["premios"].str.extract(r'(\d+)')  # Cria uma cópia da coluna pegando só os dígitos
df["premios_num"] = df["premios_num"].fillna(0).astype(int)  # Substitui NaN por 0 e converte para inteiro

premios_spilberg = df[df["diretor"] == "Steven Spielberg"]["premios_num"].sum()
print(f"Soma dos prêmios do Spilberg: {premios_spilberg}")

# É possível recuperar ainda informações "gerais" através do método describe
print(df.describe())

# Count - Número de valores não nulos
# Mean - Média dos valores
# std - Desvio padrão 
# min - valor mínimo
# 25 - primeiro quártil (Q1)
# 50 - Q2
# 75 - Q3
# max - valor máximo

# Através dessas funções são possíveis interações interessantes.

# Como por exemplo - Exportar um CSV gerado a partir da modificação de um outro
def exportar_csv(resultado, nome_arquivo):
        """Exporta o DataFrame filtrado para um CSV."""
        if resultado.empty:
            print("Nenhum dado para exportar.")
        else:
            resultado.to_csv(nome_arquivo, index=False, encoding="utf-8")
            print(f"Arquivo exportado com sucesso: {nome_arquivo}")

# Permitir que o usuário escolha os filtros a serem aplicados no csv original
def escolherFilmes():
   # Lê o CSV principal
    df = pd.read_csv("arquivos/filmes.csv", encoding="utf-8")

    while True: # Loop de interação com o usuário
        print("\n===== CONSULTA DE FILMES =====")
        print("1 - Buscar filmes por diretor")
        print("2 - Buscar filmes por ano")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            diretor = input("Digite o nome do diretor: ")
            resultado = df[df["diretor"].str.contains(diretor, case=False, na=False)] # Utiliza o método contains para avaliar se a resposta existe no csv
            if resultado.empty:
                print(f"Nenhum filme encontrado para '{diretor}'.")
            else:
                print("\nFilmes encontrados:")
                print(resultado[["titulo", "ano", "nota_imdb", "premios"]]) # Define no dataFrame gerado as colunas que devem ser exibidas
                
                salvar = input("Deseja exportar para CSV? (s/n): ").strip().lower()
                if salvar == "s":
                    nome_arquivo = f"filmes_{diretor.replace(' ', '_')}.csv"
                    exportar_csv(resultado, nome_arquivo)  # Chama a função que exporta em CSV
    
        elif opcao == "2":
            ano = input("Digite o ano (ex: 1999): ")
            if not ano.isdigit():
                print("Por favor, digite um ano válido.")
            else:
                ano = int(ano)
                resultado = df[df["ano"] == ano]
                if resultado.empty:
                    print(f"Nenhum filme encontrado para o ano {ano}.")
                else:
                    print("\nFilmes encontrados:")
                    print(resultado[["titulo", "diretor", "nota_imdb", "premios"]])
                    
                    salvar = input("Deseja exportar para CSV? (s/n): ").strip().lower()
                    if salvar == "s":
                        nome_arquivo = f"filmes_{ano}.csv"
                        exportar_csv(resultado, nome_arquivo)
        
        elif opcao == "3":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")

