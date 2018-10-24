import time
import sys
import cherrypy

from model import Model
from utils.logger import MainLogger

logger = MainLogger(__name__)


class Handler(object):

    def __init__(self):
        self.model = Model()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def default(self):
        data = cherrypy.request.json
        predictions = self.model.predict(data['input'])[0]
        return {"status": "success", "result": predictions.tolist()}


if __name__ == "__main__":

    host = sys.argv[1]
    port = int(sys.argv[2])

    cherrypy.config.update({
        'server.thread_pool': 1,
        'server.socket_host': host,
        'server.socket_port': port,
        'log.screen': False,
        'log.access_file': '',
        'log.error_file': ''
    })
    cherrypy.quickstart(Handler(), '/predict')
