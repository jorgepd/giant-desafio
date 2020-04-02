# standard imports
import os

# custom imports
from app import create_app


my_app = create_app(config_name = os.getenv('FLASK_ENV') or 'local')
