from ticketing_service.database import db
from ticketing_service.database.models import Order, Ticket


def add_ticket(order_id, data):
    status = data.get('status')
    description = data.get('description')

    order = Order.query.filter(Order.id == order_id).one()
    ticket = Ticket(status, description, order, order_id)

    db.session.add(ticket)
    db.session.commit()


def update_ticket(ticket_id, data):
    ticket = Ticket.query.filter(Ticket.id == ticket_id).one()
    ticket.status = data.get('status')
    ticket.comments = data.get('comments')

    db.session.add(ticket)
    db.session.commit()


def delete_ticket(ticket_id):
    ticket = Ticket.query.filter(Ticket.id == ticket_id).one()

    db.session.delete(ticket)
    db.session.commit()
