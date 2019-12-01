from ticketing_service.database import db
from ticketing_service.database.models import Garment, Ticket


def add_garment(ticket_id, data):
    style = data.get('style')
    color = data.get('color')
    size = data.get('size')
    quantity = data.get('quantity')

    ticket = Ticket.query.filter(Ticket.id == ticket_id).one()
    garment = Garment(style, color, size, quantity, ticket, ticket_id)

    db.session.add(garment)
    db.session.commit()


def update_garment(ticket_id, data):
    garment = Garment.query.filter(Garment.ticket_id == ticket_id).one()

    garment.style = data.get('style')
    garment.color = data.get('color')
    garment.size = data.get('size')
    garment.quantity = data.get('quantity')

    ticket_id = data.get('ticket_id')
    garment.ticket = Ticket.query.filter(Ticket.id == ticket_id).one()

    db.session.add(garment)
    db.session.commit()


def delete_garment(ticket_id):
    garment = Garment.query.filter(Garment.ticket_id == ticket_id).one()
    db.session.delete(garment)
    db.session.commit()
