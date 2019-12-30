from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    """
    Creates an application instance to run
    :return: A Flask object
    """
    return Flask(__name__)