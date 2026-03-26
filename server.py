from flask import request, Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/enviar_dados', methods=['POST'])
def receber_dados():
    dados = request.json
    print(dados)

    return jsonify({"dados_recebidos": dados}), 201

app.run()