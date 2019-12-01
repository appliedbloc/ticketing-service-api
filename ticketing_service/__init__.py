from flask import Flask


def create_app():
    """
    Creates an application instance to run
    :return: A Flask object
    """
    return Flask(__name__)