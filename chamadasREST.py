# Existem algumas maneiras de fazermos chamadas REST para o Python, uma delas é utilizando o Flask
# Flask é um microFramework que traz somente o essencial para as chamadas REST
from flask import Flask, request, jsonify

app = Flask(__name__) # Criação da aplicação para rodar na WEB

# Lista na memória
itens = []

@app.route('/itens', methods=['GET']) # Anotação de declaração da rota, Rota para listar os itens
def listar_itens():
    return jsonify(itens)  # Retorna a lista como JSON

@app.route('/itens', methods=['POST']) # Rota para adicionar um item
def adicionar_item():
    data = request.json  # Espera JSON no corpo da requisição
    if not data or 'nome' not in data: # Verifica se existem dados e se nos dados existe o parâmetro "nome", obrigatório
        return jsonify({'erro': 'Campo "nome" é obrigatório'}), 400
    
    item = {'id': len(itens) + 1, 'nome': data['nome']}
    itens.append(item)
    return jsonify(item), 201  # Retorna o item criado com status 201

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)