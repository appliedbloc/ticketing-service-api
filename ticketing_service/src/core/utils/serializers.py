from flask_restplus import fields

from ticketing_service.src.restplus import api

client = api.model('Client', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a client'),
    'client_name': fields.String(required=True, description='Client first name and last name'),
    'address': fields.String(required=True, description='Client address'),
    'client_type': fields.String(required=True, description='Type of client (Business/Personal)'),
    'order_id': fields.Integer(attribute='order.id'),
})

garment = api.model('Garment', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a task'),
    'style': fields.String(required=True, description='Garment style'),
    'color': fields.String(required=True, description='Garment color'),
    'size': fields.String(required=True, description='Garment size'),
    'quantity': fields.Integer(required=True, description='Number fo garments'),
    'ticket_id': fields.Integer(attribute='ticket.id')
})

task = api.model('Task', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a task'),
    'task_type': fields.String(required=True, description='Task type'),
    'assignee': fields.String(required=True, description='Assignee for the task'),
    'sequence_order': fields.Integer(required=True, description='Order of the task'),
    'created': fields.DateTime(readOnly=True),
    'ticket_id': fields.Integer(attribute='ticket.id')
})

ticket = api.model('Ticket', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a ticket'),
    'status': fields.String(required=True, description='Status of the ticket'),
    'created': fields.DateTime(readOnly=True, description='Ticket creation timestamp'),
    'description': fields.String(required=True, description='Description of this ticket'),
    'order_id': fields.Integer(attribute='order.id')
})

order = api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an order'),
    'status': fields.String(required=True, description='Status of the order'),
    'created': fields.DateTime(readOnly=True, description='Order creation timestamp'),
    'description': fields.String(required=True, description='Description of this order')
})

order_detailed = api.inherit('Detailed Order', order, {
    'clients': fields.List(fields.Nested(client)),
    'tickets': fields.List(fields.Nested(ticket)),
})

ticket_detailed = api.inherit('Detailed Ticket', ticket, {
    'garments': fields.List(fields.Nested(garment)),
    'tasks': fields.List(fields.Nested(task))
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})
