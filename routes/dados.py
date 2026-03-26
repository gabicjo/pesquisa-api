from flask import Blueprint, request, jsonify
from models.banco import receber_dados_da_api

dados_bp = Blueprint("receber_dados", __name__)

@dados_bp.route('/enviar_dados', methods=['POST'])
def receber_dados():
    dados_recebidos = request.get_json()

    if not dados_recebidos:
        return jsonify({"erro": "JSON vazio ou não enviado"}), 400

    print(dados_recebidos)

    receber_dados_da_api(dados_recebidos)

    return jsonify({"dados_recebidos": dados_recebidos}), 201