import pytest
from app import create_app

@pytest.fixture(scope='module')
def create_app_setup():
    app = create_app()
    with app.test_client() as test_client:
        yield test_client