from flask import Blueprint

return_calculator_api = Blueprint('return_calculator_endpoint', __name__)

from . import return_calculator_endpoint
