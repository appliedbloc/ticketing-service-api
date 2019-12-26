import logging

from ticketing_service.database import db
from ticketing_service.database.models import Order, Client

log = logging.getLogger(__name__)


def add_client(order_id, data):
    client_name = data.get('client_name')
    address = data.get('address')
    client_type = data.get('client_type')

    order = Order.query.filter(Order.id == order_id).one()
    client = Client(client_name, address, client_type, order, order_id)

    db.session.add(client)
    db.session.commit()


def update_client(order_id, data):
    client = Client.query.filter(Client.order_id == order_id).one()

    client.client_name = data.get('client_name')
    client.address = data.get('address')
    client.client_type = data.get('client_type')

    order_id = data.get('order_id')
    client.order = Order.query.filter(Order.id == order_id).one()

    db.session.add(client)
    db.session.commit()


def delete_client(order_id):
    client = Client.query.filter(Client.order_id == order_id).one()

    db.session.delete(client)
    db.session.commit()
