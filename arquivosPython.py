import csv

# Em Python é possível acessar, manipular e gerar arquivos de forma ágil e simples
# Leva-se em consideração a estrutura Header (cabeçalho com metaDados do arquivo)
# Dados (Conteúdo do arquivo)
# EOF (caracter especial que marca o fim do arquivo, End of File)

# A manipulação segue a lógica de abrir o arquivo - manipular o arquivo - fechar o arquivo
# São abertos através do método open, que pode receber além do caminho do arquivo parâmetros que indicam que é modo de leitura, edição ou qualquer outro

arquivo = open('arquivos/teste.txt') # Por padrão abre em r, modo de leitura
arquivo = open('arquivos/texte.txt','w') # abrir em modo de escrita
arquivo = open('arquivos/texte.txt','r+b') # ler e escrever no modo binário

# Depois de realizar as operações é necessário liberar os recursos através do método close
arquivo.close()

# Para garantir que o método foi executado corretamente, incluindo a codifição, é interessante colocar em um try/catch
try:
    f = open("teste.txt", encoding = 'utf-8') # Indicando o encoding
finally:
    f.close()

# É possível escrever em arquivos utilziando o método write (pode sobrescrever o que já existia).
# Escrevendo no arquivo
with open("arquivos/teste.txt", 'w', encoding='utf-8') as arquivo: # O arquivo é automaticamente fechado depois do bloco with
    arquivo.write("Estamos escrevendo no arquivo\n")
    arquivo.write("Outra linha escrita no arquivo\n")

# Lendo e imprimindo o conteúdo
with open("arquivos/teste.txt", 'r', encoding='utf-8') as arquivo:  # É interessante separar a leitura da escrita e da impressão!
    print(arquivo.read()) # Read é utilizado para ler arquivos

# Anexando (append) a um arquivo:
with open("arquivos/teste.txt",'a', encoding='utf-8') as arquivo:
    arquivo.write("Texto anexado através do parametro 'a'")

with open("arquivos/teste.txt",'r', encoding='utf-8') as arquivo:
    print(arquivo.read()) # Read é utilizado para ler arquivos

# É possível interagir com arquivos de diversos formatos, possibilitando diversas operaçõe
with open('arquivos/filmes.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file) # O Método DictReader() retorna um objeto csv.DictReader que podemos iterar e percorrer os valores através de um for loop
    for linha in csv_reader:
        print(f"{linha['titulo']} | {linha['ano']} | {linha['diretor']} | {linha['genero']} | {linha['duracao_min']} | {linha['nota_imdb']} | {linha['estudio']} | {linha['premios']}")

