# Tuplas são uma sequência de objetos imutáveis, em outras palavras, uma vez criadas, tuplas não podem ser modificadas, normalmente são usadas para guardar dados protegidos.
from collections import namedtuple

estudantes = ('João','Maria','Fernanda','Lucas','Alisson','Davi')
print(estudantes) # Imprimindo a tupla
print([estudante for estudante in estudantes]) # imprimindo os valores de tupla como lista
print('João' in estudantes) # Checando se o valor "João" existe na tupla
print('João' not in estudantes) # Checando se o valor "João" NÃO existe na tupla
print(len(estudantes)) # 6 - Imprime o tamanho da tupla

# Pode-se utilziar del para deletar uma tupla
del(estudantes);print(estudantes) # Após exclusão : NameError: name 'estudantes' is not defined

# É possível criar uma tupla através do método tuple
numeros = tuple(x for x in range(1,20,3)); print(numeros) # (1, 4, 7, 10, 13, 16, 19)

# Método count
print(numeros.count(7)) # 1 - A função 'count' avalia quantas vezes um elemento aparece numa tupla

# Método index permite procurar por um elemento na tupla e retorna em qual índice ele foi encontrado
numeros.index(4) # 1

# Um outro tipo de Tupla é a nammedTouple, que serve para nomear tuplas e permitir acesso através do nome dos campos além do indice
Universitario = namedtuple('Estudante', ['nome', 'idade', 'nota']) # Criando a estrutura da tupla

joao = Universitario(nome='João', idade=20, nota=8.5) # Criando instâncias
maria = Universitario(nome='Maria', idade=22, nota=9.3)
amanda = Universitario(nome='Amanda', idade=25, nota=10.0)

print(joao) # Imprimindo a tupla joao
print(amanda.nome) # Imprimindo o valor "nome" da tupla amanda
print(amanda.nota) # Imprimindo a nota da tupla amanda