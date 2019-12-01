from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from ticketing_service.database.models import Task, Ticket
    db.drop_all()
    db.create_all()
