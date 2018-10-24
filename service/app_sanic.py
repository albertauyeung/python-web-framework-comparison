import sys
from sanic import Sanic
from sanic.response import json

from model import Model
from utils.logger import MainLogger

logger = MainLogger(__name__)

app = Sanic()
app.model = Model()


@app.route('/predict', methods=['POST'])
async def predict(request):
    data = request.json
    predictions = request.app.model.predict(data['input'])[0]
    return json({"status": "success", "result": predictions.tolist()})


if __name__ == "__main__":

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=False, access_log=False)
