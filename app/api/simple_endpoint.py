# standard imports
from flask_apispec import doc

# custom imports
from . import simple_endpoint_api
from app import logger


@simple_endpoint_api.route('/hello', methods=['GET'], provide_automatic_options=False)
@doc(tags=['Simple Endpoint'], description='Say Hello')
def hello():
    logger.info('Called "Say Hello" function')
    return 'Hello, World!!'
