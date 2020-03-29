# standard imports
import logging.config
import logging
import yaml
import sys

from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec

# custom imports
from app.config import CONFIG

# global variables
logger = None


def create_app(config_name=None):
    # app
    app = Flask(__name__)

    # configure logger
    init_logger(app)
    logger.info('Creating app...')

    # configs
    config = CONFIG[config_name](app)
    config.init_app()
    app.config.from_object(config)

    # define API specifications
    app.config.update({
    'APISPEC_SPEC': APISpec(
        title='flask_api',
        version=app.config.get('VERSION'),
        openapi_version='2.0',
        plugins=[
            MarshmallowPlugin()
        ]
    ),
    'APISPEC_SWAGGER_UI_URL': '/api/swagger'
    })

    # register app endpoints
    register_endpoints(app)

    # app documentation
    docs = FlaskApiSpec()
    docs.init_app(app)
    document_endpoints(docs)
    logger.info('App created')

    return app

def init_logger(app):
    # configure app logger
    conf_dict = yaml.load(open('logging.conf'), Loader=yaml.FullLoader)
    logging.config.dictConfig(conf_dict)

    global logger
    logger = app.logger

def register_endpoints(app):
    # simple endpoint
    from .api.simple_endpoint import simple_endpoint_api

    app.register_blueprint(simple_endpoint_api, url_prefix='/api')

def document_endpoints(docs):
    # simple endpoint
    from .api.simple_endpoint import hello

    docs.register(hello, blueprint='simple_endpoint')