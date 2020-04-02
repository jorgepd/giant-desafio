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
logger = logging.getLogger()


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
        title='return_calculator_api',
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
    logger.info(f'App created with {config_name} config')

    return app

def init_logger(app):
    # configure app logger
    conf_dict = yaml.load(open('logging.conf'), Loader=yaml.FullLoader)
    logging.config.dictConfig(conf_dict)

    global logger
    logger = app.logger

def register_endpoints(app):
    # return calculator
    from .api import return_calculator_api

    app.register_blueprint(return_calculator_api, url_prefix='/api')

def document_endpoints(docs):
    # return calculator functions
    from .api.return_calculator_endpoint import _absolute_return, _relative_return,\
        _biggest_return, _smallest_return, _cummulative_returns, _equity_evolution

    # return calculator endpoints
    docs.register(_absolute_return, blueprint='return_calculator_endpoint')
    docs.register(_relative_return, blueprint='return_calculator_endpoint')
    docs.register(_biggest_return, blueprint='return_calculator_endpoint')
    docs.register(_smallest_return, blueprint='return_calculator_endpoint')
    docs.register(_cummulative_returns, blueprint='return_calculator_endpoint')
    docs.register(_equity_evolution, blueprint='return_calculator_endpoint')
