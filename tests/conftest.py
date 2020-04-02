# standard imports
import pytest

# custom imports
from app import create_app


@pytest.fixture()
def test_app():
    app = create_app('test')
    return app
