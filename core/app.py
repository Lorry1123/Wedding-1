import sys
import traceback

from flask import Flask, jsonify, request
import logging

from werkzeug.exceptions import HTTPException

from core.exceptions import PlatformException
from core.view.api import api_bp
from core.view.web import web_bp


logger = logging.getLogger(__name__)


def init_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel("INFO")
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)-8s]  [%(module)-10s:%(lineno)5d]  "
                                  "[%(process)d] [%(thread)d] %(message)s")
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
    app.register_blueprint(web_bp)


def create_app():
    init_logging()
    app = Flask("Wedding")
    app.config["PROPAGATE_EXCEPTIONS"] = True
    init_blueprint(app)
    init_error_handler(app)
    return app


app = create_app()


@app.before_request
def func():
    url = request.path
    method = request.method
    body = request.get_json()
    logger.info("Received a new request. %s %s, Body:%s", method, url, body)
