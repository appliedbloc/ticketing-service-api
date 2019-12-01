import logging

from ticketing_service.database import db
from ticketing_service.database.models import Client, Ticket

log = logging.getLogger(__name__)


def add_client(ticket_id, data):
    client_name = data.get('client_name')
    address = data.get('address')
    client_type = data.get('client_type')

    ticket = Ticket.query.filter(Ticket.id == ticket_id).one()
    client = Client(client_name, address, client_type, ticket, ticket_id)

    db.session.add(client)
    db.session.commit()


def update_client(ticket_id, data):
    client = Client.query.filter(Client.ticket_id == ticket_id).one()

    client.client_name = data.get('client_name')
    client.address = data.get('address')
    client.client_type = data.get('client_type')

    ticket_id = data.get('ticket_id')
    client.ticket = Ticket.query.filter(Ticket.id == ticket_id).one()

    db.session.add(client)
    db.session.commit()


def delete_client(ticket_id):
    client = Client.query.filter(Client.ticket_id == ticket_id).one()

    db.session.delete(client)
    db.session.commit()
