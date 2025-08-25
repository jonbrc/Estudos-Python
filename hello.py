
# Variaveis em Python são dinamicamente tipadas e não podem começar com números
variavelTeste = "Hello Word"
variavelTeste = 4 # Apesar de ser dinamicamente tipado alterações de tipo ao longo da execução não causam erros
print(variavelTeste)

# É possível definir várias variaveis numa mesma linha
x,y,z = 10,"Teste",1.87

print(x)
print(y)
print(z)

# Não é possível definir constantes em python, caso a necessidade é que uma varíavel comporte-se como tal é necessário nomea-la com letras maiúsculas por convenção

# A indentação define o bloco de código, por isso é parte fundamental do script
vida = 100
if vida > 50:
    print("Você está vivo")

# Em python temos o uso de statements, continuações de execução de um bloco de código em diferentes linhas
total = 3 + \
    5 + \
    7
print(total) 

# Utilizando ponto e vírgula é possível termos vários pontos na mesma linha
x,y = 10,6 ; z = x * y; print(f'{x} x {y} = {z}') ## Nesse caso utiliza-se a sintaxe fString, que permite a criação de placeholders dentro de uma string

# Por ser uma Linguagem orientada a objetos comporta-se de forma semelhante a java no que tange ao fato de atribuir à variáveis não valores, mas sim ponteiros para os valores armazenados em memória
x = 33 # cria-se um objeto em memória com o valor 33 e atribuie a x o ponteiro para tal
y = x # não cria-se outro objeto, mas atribui a y o mesmo ponteiro
y = 33 # nesse caso um novo objeto não necessariamente será criado pois objetos pequenos são armazenados no cache

print(id(x))
print(id(y)) # A função "id" imprime o endereço de objetos, apesar de serem declarados individualmente ambos tem o mesmo valor

# Qualquer variável declarada fora do escopo de uma função é considerada global e pode ser acessada dentro de funções, por outro lado seu valor não pode ser alterado dentro delas

x = 3
def add():  # Caso essa função seja executada o seguinte erro aparecerá no console: UnboundLocalError: cannot access local variable 'x' where it is not associated with a value 
    x = x + 5
    print(x)

# Para contornar esse erro é possível recuperar a variável e utliza-la no escopo da função através da keyWord Global
def add():
    global x
    x = x + 5
    print(x)
add()

# Falando agora de Strings o Python oferece muitos recursos interessantes de manipulação e controle, assim como em muitas linguagens o String é interpretado como um Array
 #de bytes. Outro ponto é que não existe o tipo primitivo char, um char é interpretado como uma string de tamanh 1 (ou 0)

nome = "joão bruno reis"

print(nome[0]) # J
print(nome[1]) # o
print(nome[2]) # ã
print(nome[3]) # o
#print(nome[500]) - Exibirá o erro "indexError: string index out of range"

# Por conta dessa peculiaridade, é possível também imprimir uma substring passando o índice inicial e o final

print(nome[2:10]) # ao Bruno

# O método strip retira os espaços no começo e no fim da String
print(nome.strip())

# O método len retorna o tamanho da string
print(len(nome))

# A seguinte abordagem inverte a string
print(nome[::-1])

# Os métodos lower e upper servem, respectivamente para deixar minusculos e maiusculos. o método case inverte a case de cada indice da string
print(nome.lower(),nome.upper())

# O método title transforma cada indice inicial em upperCase
print(nome.title())

# O método replace é utilziado para substituir trechos da String e espera dois argumentos, a string procurada e a string que a substituirá
print(nome.replace("joão","josé"))

# O método split separa a string em sub-strings em função de um separado e retorna um iterável
print(nome.split(" ")) # nesse caso separando por " "


# O método Input permite com que o script receba dados do usuário
n = input("Insira um número: ")
print(n)