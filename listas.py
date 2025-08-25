# Python oferece 4 principais estruturas de dados. 1 - Listas, 2 - tuplas, 3 - dicionários e 4 - Sets

# 1 - Listas: Listas são conjuntos ordenados e mutáveis que permitem duplicação, via de regra é a estrutura mais flexível
nomes = ["joão","Amanda","Maria","Marcos","Chokito","Zumzos","Pescoço"]
print(nomes)
print(len(nomes))

# Atráves do conceito de splicing é possível acessar elementos específicos da lista
print(nomes[1:4])

# Partindo desse conceito utiliza-se uma sintaxe que facilita o ato de percorrer a lista:
# lista[inicio:parada] # item de inicio até o item de parada - 1
#lista[inicio:] # item de inicio até o fim da lista
#lista[:parada] # itens do começo da lista até parada - 1
#lista[:] # cópia da lista inteira

# É possível unir os elementos de uma lista através do método join. No exemplo abaixo a junção acontece separando os elements por '-'
nomesJoin = '-'.join(nomes)
print(nomesJoin)

# Seguindo essa lógica é possível alterar e manipular elementos de uma lista através de operações
materias = ["Física"]
print(materias[0])

materias += ["Biologia","Matemática"]
print(materias)

for materia in materias:
    print(materia)

# o método in avalia se um valor está ou não em uma lista e retorna um booleano
print("Biologia" in materias) ; print("Cosmologia" in materias)

# Para adicionar um item a uma lista temos o método append, que posiciona um novo elemento no fim da lista
materias.append("Química"); print(materias)

# Temos o método extend, que pode adicionar vários elementos também no fim da lista
materias.extend(["Geografia","História da arte"]); print(materias)

# O método insert permite adicionar um elemento em um local específico da lista
materias.insert(1,"Educação física"); print(materias)

# Para remover um iten de uma lista podemos seguir alguns caminhos, por exemplo, Pop para remover o último elemento
materias.pop(); print(materias)

# Pode-se usar o método del, passando um índice para remover um indice espécifico
del(materias[0]); print(materias)

# Pode-se usar o método remove para buscar um elemento específico da lista, no caso de múltiplas ocorrências ele removerá o primeiro encontrado
materias.remove("Biologia"); print(materias) # Caso não encontre o elemento é lançada uma exceção

# Por fim tem-se o método clear, que limpa a lista completamente
materias.clear(); print(materias)

# Existem diversas maneiras de operar com listas
inteiros = [1,2,3,4,5,6,7]
negativos = [-7,-4,-6,-4,-11,-3,-1]
primos = [1,3,5,7,9,13]
hibrida = [8,10,56,"Joao",False]

concat = inteiros + negativos; print(concat) # [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, -7] - juntando as listas
print(inteiros * 2) # [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7] - duplicando cada elemento
concat.sort();print(concat) # [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7] - Ordenando a lista
hibrida.sort();print(hibrida) # Retorna erro pois não é possível ordendar strings e booleanos
print(sorted(negativos)) # Diferente de sort, sorted cria uma nova lista ao invés de alterar a original
print(sorted(negativos,reverse=True)) # Ainda é possível usar o parâmetro reverse para inverter a ordem no método sorted

# Entendendo esses pontos podemos chegar no conceito de list comprehension, que é a construção de uma lista a partir de um outro interável
valores = [-5, 7, 1, 0, 10, 100, 33, 2]
print([v**2 for v in valores])  # [25, 49, 1, 0, 100, 10000, 1089, 4] - Na prática, o que acontece é um loop for feito de forma condensada criando uma lova lista

# Todo list interaction tem 3 membros: 1 - Expressão, 2 - Membro, 3 - Interável
print([v/2 for v in valores])
print([v+10 for v in valores]) # expressão = v + 10; membro = v; interável = valores
print([v*1.32 for v in valores]) 

# Além dessas operações é possível realizar testes como if dentro do list comprehension

print([v*2 for v in valores]) # [-10, 14, 2, 0, 20, 200, 66, 4]
print([v*2 for v in valores if v%2 == 0]) # [0, 20, 200, 4] - Imprimindo somente os valores "v" que são pares
print ([v*2 for v in valores if v*2 >= 20]) # [20, 200, 66] - Imprimindo só o que for >= 20

# Exemplo prático - Lógica de transformação de celsius para fahrenheit 
celsius = [21.7,33,31,16,12.4,-34]
fahrenheit = [round((9/5)*t + 32, 2) for t in celsius]
print(fahrenheit)

# Também é possível fazer produto entre os elementos de listas além de somas, como por exemplo o método sum
soma = sum([n for n in range(10)]); print(soma) # 45 Soma dos elementos no range
print(sum([n for n in inteiros])) # 28 soma dos elementos na lista inteiros
print(sum([n for n in hibrida])) # Erro por não pode somar ints e strings

lista1 = [10,20,31,50,15]
lista2 = [4,100,32,56,12]

somas = [a + b for a, b in zip(lista1, lista2)]; print(somas) # [14, 120, 63, 106, 27] Somando item a item
print(sum(lista1) + sum(lista2)) # 330 Soma do total das listas

# Zip() serve para empacotar elementos de dois conjuntos de dados em pares da seguinte forma:
lista1 = [1,2,3]
lista2 = ['a','b','c']

pares = zip(lista1,lista2)

for par in pares:
    print(par)  # resultado - (1,'a'),(2,'b'),(3,'c')