from flask import Blueprint

simple_endpoint_api = Blueprint('simple_endpoint', __name__)

from . import simple_endpoint
