from fastapi import FastAPI

from src.core.config import get_settings

settings = get_settings()


def test_main_create_app_should_return_instance_fastapi_when_called():
    from src.main import create_app

    app = create_app()

    assert isinstance(app, FastAPI)
    assert app.title == settings.APP_NAME
    assert app.version == settings.APP_VERSION
    assert app.description == settings.APP_DESCRIPTION
    assert app.root_path == settings.ROOT_PATH
