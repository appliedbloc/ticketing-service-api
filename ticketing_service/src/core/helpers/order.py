from ticketing_service.database import db
from ticketing_service.database.models import Order


def create_order(data):
    status = data.get('status')
    description = data.get('description')

    order = Order(status, description)

    db.session.add(order)
    db.session.commit()


def update_order(order_id, data):
    order = Order.query.filter(Order.id == order_id).one()
    order.status = data.get('status')
    order.description = data.get('description')

    db.session.add(order)
    db.session.commit()


def delete_order(order_id):
    order = Order.query.filter(Order.id == order_id).one()

    db.session.delete(order)
    db.session.commit()
