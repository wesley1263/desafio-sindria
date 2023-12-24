import pytest
from fastapi.testclient import TestClient

from src.core.config import get_settings
from src.main import create_app

settings = get_settings()
settings.TESTING = True
app = create_app()


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as test_client:
        yield test_client
