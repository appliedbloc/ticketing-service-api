from ticketing_service.app import initialize_app, app
from ticketing_service.database import reset_database

initialize_app(app)
with app.app_context():
    reset_database()
