from flask import Flask, jsonify, request


app = Flask(__name__)

garagem = [
    {
        'id': 1,
        'marca': 'volkswagem',
        'modelo': 'gol 1.0',
        'ano': '2010',
        'cor': 'branco',
        'preco': 'R$ 25.000',
    },

    {
        'id': 2,
        'marca': 'chevrolet',
        'modelo': 'astra sedan advantage',
        'ano': '2011',
        'cor': 'preto',
        'preco': 'R$ 31.701',
    },

    {
        'id': 3,
        'marca': 'toyota',
        'modelo': 'Corolla Altis Hybrid 1.8 16V Fle',
        'ano': '2020',
        'cor': 'chumbo',
        'preco': 'R$ 153.858',
    }
]

# create
@app.route('/garagem', methods=['POST'])
def incluir_novo_veiculo():
    novo_veiculo = request.get_json()
    garagem.append(novo_veiculo)
    return jsonify(garagem)

# read all
@app.route('/garagem/', methods=['GET'])
def obter_veiculos():
    return jsonify(garagem)

# read with id
@app.route('/garagem/<int:id>', methods=['GET'])
def obter_veiculos_por_id(id):
    for veiculo in garagem:
        if veiculo.get('id') == id:
            return jsonify(veiculo)

# update
@app.route('/garagem/<int:id>', methods=['PUT'])
def editar_garagem_por_id(id):
    veiculo_alterado = request.get_json()
    for indece,veiculo in enumerate(garagem):
        if veiculo.get('id') == id:
            garagem[indece].update(veiculo_alterado)
            return jsonify(garagem[indece])

# delete
@app.route('/garagem/<int:id>', methods=['DELETE'])
def excluir_veiculo(id):
    for indice, veiculo in enumerate(garagem):
        if veiculo.get('id') == id:
            del garagem[indice]
        return jsonify(garagem)

app.run(port=5000, host='localhost', debug=True)