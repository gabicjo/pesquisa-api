from flask import request, Flask, jsonify
from flask_cors import CORS
from routes.dados import dados_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(dados_bp)

app.run(port=5001)
