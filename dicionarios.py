# Dicionários são estruturas que fazem relação chave - valor 
Estudante = {
    'nome':'João Bruno',
    'matricula':'200026858',
    'escola':'tecnologia',
    'matriz':2023,
    'curso':'Engenharia de software'
}

print(Estudante)
print(Estudante['nome']) # Imprimindo o nome do estudante
print(Estudante['matriz'])
print(Estudante['curso'])

# É possível acessar os atributos do objeto através da sintaxe nomeObjeto['NomeAtributo'], possibilitando além de consultas alterações em seus valores
Estudante['escola'] = 'Tecnlogias';print(Estudante['escola'])

# De maneira semelhante é possível adicionar itens ao dicionpario
Estudante['media'] = 9.56; print(Estudante)
