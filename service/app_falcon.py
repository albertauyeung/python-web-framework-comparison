import sys
import json
import falcon

from model import Model
from utils.logger import MainLogger

logger = MainLogger(__name__)


class Handler(object):

    def __init__(self):
        self.model = Model()

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        predictions = self.model.predict(data['input'])[0]
        resp.media = {
            "status": "success",
            "result": predictions.tolist()
        }

app = falcon.API()
app.add_route('/predict', Handler())


if __name__ == "__main__":

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port)
