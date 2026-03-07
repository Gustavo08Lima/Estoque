#API  - é um lugar para disponibilizar recursos ou funcionalidades

# Objetivo - criar uma api que armazena, consulta, altera e deleta dados

# URL base - localhost

# Endpoints -
    # - Localhost/livros(get)
    # - Localhost/livros/id(get)
    # - Localhost/livros/id(put)
    # - Localhost/livros/id(put)

from flask import Flask, jsonify, request
import json
import os

gustavo = Flask(__name__)
ARQUIVO_DADOS = 'dados.json'

def ler():
    with open(ARQUIVO_DADOS, 'r') as f:
        return json.load(f)
    
def salvar():
    with open(ARQUIVO_DADOS,'w') as f:
        json.dump(dados,f,indent=4)

saquinho = [
            {
            "id": 1,
            "nome": "Vermelho",
            },
            {
            "id": 2,
            "nome": "PRETO",
            }
]    

@gustavo.route('/saquinho',methods=['GET'])

def obter():
    return jsonify(saquinho)


@gustavo.route('/saquinho/<int:id>',methods=['GET'])
def obter_id(id):
    for item in saquinho:
        if item.get('id') == id: 
            return jsonify(item)
        

@gustavo.route('/saquinho/<int:id>',methods=['PUT'])
def edita_id(id):
    saquinho_alterado = request.get_json()
    for indice,item in enumerate(saquinho):
        if item.get('id') == id:
            saquinho[indice].update(saquinho_alterado)
            return jsonify(saquinho[indice])
        
@gustavo.route('/saquinho',methods=['POST'])
def criar():
    new = request.get_json()
    saquinho.append(new)

    return jsonify(saquinho)

@gustavo.route('/saquinho/<int:id>',methods=['DELETE'])
def excluir(id):
    for indice, item in enumerate (saquinho):
        if item.get('id') == id:
            del saquinho[indice]
    return jsonify(saquinho)


# No final do seu arquivo, substitua o gustavo.run(...) por:
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    gustavo.run(host='0.0.0.0', port=port)