from flask import Blueprint, request, jsonify

dados_bp = Blueprint("receber_dados", __name__)

@dados_bp.route('/enviar_dados', methods=['POST'])
def receber_dados():
    dados = request.json

    if not dados:
        return jsonify({"erro": "JSON vazio ou não enviado"}), 400

    print(dados)

    return jsonify({"dados_recebidos": dados}), 201