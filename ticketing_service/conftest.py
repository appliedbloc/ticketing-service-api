import pytest
from flask import Flask


@pytest.fixture
def app() -> Flask:
    """ Provides an instance of our Flask app """
    from ticketing_service import create_app

    return create_app()
