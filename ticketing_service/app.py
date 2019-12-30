import logging.config
import os

from flask import Flask, Blueprint

from ticketing_service import login_manager
from ticketing_service import settings
from ticketing_service.database import db
from ticketing_service.src.core.endpoints.auth import ns as auth_namespace
from ticketing_service.src.core.endpoints.orders import ns as orders_namespace
from ticketing_service.src.core.endpoints.tickets import ns as tickets_namespace
from ticketing_service.src.restplus import api

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

app.secret_key = "6080f3f8-e7b2-457b-b52c-fbfb877fab29"  # Make this long, random, and secret in a real app!


def configure_app(flask_app):
    #   flask_app.config['SERVER_NAME'] = settings.FLASK_DEV_SERVER
    flask_app.config['TESTING'] = settings.TESTING
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(auth_namespace)
    api.add_namespace(orders_namespace)
    api.add_namespace(tickets_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    login_manager.init_app(app)


def main():
    initialize_app(app)
    #    log.info('Starting development server at http://{}/api/'.format(app.config['SERVER_NAME']))
    app.run(threaded=True, host='0.0.0.0', port=8888)


#    app.logger.setLevel(logging.INFO)


if __name__ == "__main__":
    main()
