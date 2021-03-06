from datetime import datetime

from ticketing_service.database import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = db.relationship('Order', backref=db.backref('clients', lazy='dynamic'))

    client_name = db.Column(db.String(50))
    address = db.Column(db.Text())
    client_type = db.Column(db.String(50))

    def __init__(self, client_name, address, client_type, order, order_id):
        self.client_name = client_name
        self.address = address
        self.client_type = client_type
        self.order_id = order_id
        self.order = order

    def __repr__(self):
        return '<Client %r>' % self.client_name


class TicketComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    ticket = db.relationship('Ticket', backref=db.backref('ticketComments', lazy='dynamic'))

    details = db.Column(db.String(150))
    created = db.Column(db.DateTime)
    reporter = db.Column(db.String(80))

    def __init__(self, details, created, reporter, ticket, ticket_id):
        self.details = details
        if created is None:
            created = datetime.utcnow()

        self.created = created
        self.reporter = reporter
        self.ticket_id = ticket_id
        self.ticket = ticket

    def __repr__(self):
        return '<Ticket Comment %r>' % self.client_name


class OrderComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = db.relationship('Order', backref=db.backref('orderComments', lazy='dynamic'))

    details = db.Column(db.String(150))
    created = db.Column(db.DateTime)
    reporter = db.Column(db.String(80))

    def __init__(self, details, created, reporter, order, order_id):
        self.details = details
        if created is None:
            created = datetime.utcnow()

        self.created = created
        self.reporter = reporter
        self.order_id = order_id
        self.order = order

    def __repr__(self):
        return '<Order Comment %r>' % self.client_name


class Garment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    ticket = db.relationship('Ticket', backref=db.backref('garments', lazy='dynamic'))

    style = db.Column(db.String(50))
    color = db.Column(db.String(50))
    size = db.Column(db.String(50))
    quantity = db.Column(db.Integer)

    def __init__(self, style, color, size, quantity, ticket, ticket_id):
        self.style = style
        self.color = color
        self.size = size
        self.quantity = quantity
        self.ticket_id = ticket_id
        self.ticket = ticket

    def __repr__(self):
        return '<Garment %r>' % self.style


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    ticket = db.relationship('Ticket', backref=db.backref('tasks', lazy='dynamic'))

    task_type = db.Column(db.String(80))
    assignee = db.Column(db.String(80))
    sequence_order = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __init__(self, task_type, assignee, sequence_order, ticket, ticket_id, created=None):
        self.task_type = task_type
        self.assignee = assignee
        self.sequence_order = sequence_order
        self.ticket_id = ticket_id
        self.ticket = ticket

        if created is None:
            created = datetime.utcnow()

        self.created = created

    def __repr__(self):
        return '<Task %r>' % self.task_type


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = db.relationship('Order', backref=db.backref('tickets', lazy='dynamic'))

    status = db.Column(db.String(50))
    created = db.Column(db.DateTime)
    description = db.Column(db.Text())

    def __init__(self, status, description, order, order_id, created=None):
        self.status = status
        if created is None:
            created = datetime.utcnow()

        self.created = created
        self.description = description
        self.order_id = order_id
        self.order = order


def __repr__(self):
    return '<Ticket %r>' % self.id


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))
    created = db.Column(db.DateTime)
    description = db.Column(db.Text())

    def __init__(self, status, description, created=None):
        self.status = status
        if created is None:
            created = datetime.utcnow()

        self.created = created
        self.description = description

    def __repr__(self):
        return '<Order %r>' % self.id
