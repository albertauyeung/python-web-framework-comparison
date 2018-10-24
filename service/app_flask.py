import sys
from flask import Flask, request, jsonify, current_app

from model import Model
from utils.logger import MainLogger

logger = MainLogger(__name__)

app = Flask(__name__)
app.model = Model()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    predictions = current_app.model.predict(data['input'])[0]
    return jsonify(status="success", result=predictions.tolist())


if __name__ == "__main__":

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port)
