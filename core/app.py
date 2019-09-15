import sys
import traceback

from flask import Flask, jsonify
import logging

from gevent.pywsgi import WSGIServer
from werkzeug.exceptions import HTTPException

from core.exceptions import PlatformException
from core.view.api import api_bp


logger = logging.getLogger(__name__)


def init_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel("INFO")
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)-8s]  [%(module)-10s:%(lineno)5d]  "
                                  "[%(thread)d] %(message)s")
    handler.setFormatter(formatter)

    log = logging.getLogger()
    log.addHandler(handler)
    log.setLevel(logging.INFO)


def handle_platform_exception(e):
    code = 500
    if isinstance(e, PlatformException):
        code = e.code

    if isinstance(e, HTTPException):
        code = e.code

    logger.exception(e)
    exc = traceback.format_exc()
    return jsonify({'error': str(e), 'traceback': exc}), code


def init_error_handler(app):
    app.register_error_handler(Exception, handle_platform_exception)


def init_blueprint(app):
    app.register_blueprint(api_bp)


def create_app():
    init_logging()
    app = Flask("Wedding")
    init_blueprint(app)
    init_error_handler(app)
    return app


if __name__ == "__main__":
    app = create_app()
    http_server = WSGIServer(('0.0.0.0', 9002), app)
    http_server.serve_forever()
