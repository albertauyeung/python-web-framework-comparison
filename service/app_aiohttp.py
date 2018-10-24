import sys
from aiohttp import web

from model import Model
from utils.logger import MainLogger

logger = MainLogger(__name__)


async def handle(request):
    data = await request.json()
    predictions = request.app['model'].predict(data['input'])[0]
    return web.json_response({
        "status": "success",
        "result": predictions.tolist()
    })


if __name__ == "__main__":

    app = web.Application()
    app.router.add_post('/predict', handle)
    app["model"] = Model()

    host = sys.argv[1]
    port = int(sys.argv[2])
    web.run_app(app, host=host, port=port)
