from flask import request
from flask_restplus import Resource

from ticketing_service.src.core.helpers.client import *
from ticketing_service.src.core.helpers.garment import *
from ticketing_service.src.core.helpers.task import *
from ticketing_service.src.core.helpers.ticket import *
from ticketing_service.src.core.utils.serializers import client, garment, task, ticket, ticket_detailed
from ticketing_service.src.restplus import api
from ticketing_service.database.models import Client, Garment, Task, Ticket

log = logging.getLogger(__name__)

ns = api.namespace('tickets', description='CRUD ticket operations')


@ns.route('/')
class TicketCollection(Resource):

    @api.marshal_list_with(ticket)
    def get(self):
        """
        Returns list of tickets.
        """
        log.info('Listing all tickets')

        tickets = Ticket.query.all()
        return tickets

    @api.response(201, 'Ticket successfully created.')
    @api.expect(ticket)
    def post(self):
        """
        Creates a new ticket.
        """
        data = request.json
        create_ticket(data)
        return 'Ticket successfully created.', 201


@ns.route('/<int:id>')
@api.response(404, 'Ticket not found.')
class TicketItem(Resource):

    @api.marshal_with(ticket_detailed)
    def get(self, id):
        """
        Returns a single ticket item.
        """
        log.info('Looking up ticket')

        return Ticket.query.filter(Ticket.id == id).one()

    @api.expect(ticket)
    @api.response(204, 'Ticket successfully updated.')
    def put(self, id):
        """
        Updates a ticket.
        """
        data = request.json
        update_ticket(id, data)
        return None, 204

    @api.response(204, 'Ticket successfully deleted.')
    def delete(self, id):
        """
        Deletes a ticket.
        """
        delete_ticket(id)
        return None, 204


@ns.route('/<int:id>/tasks')
@api.response(404, 'Ticket tasks not found.')
class TicketTasksCollection(Resource):

    @api.marshal_with(task)
    def get(self, id):
        """
        Retrieves list of tasks for the given ticket
        """
        log.info('Looking up tasks for ticket')

        return Task.query.filter(Task.ticket_id == id).all()


@ns.route('/<int:id>/tasks/add')
@api.response(500, 'Ticket task creation failed.')
class TicketTasksAddition(Resource):

    @api.response(201, 'Task successfully added.')
    @api.expect(task)
    def post(self, id):
        """
        Creates a new task and adds it to the given ticket
        """
        data = request.json
        add_task(id, data)
        return 'Task successfully added.', 201


@ns.route('/<int:id>/client')
@api.response(404, 'Ticket tasks not found.')
class TicketClientCollection(Resource):

    @api.marshal_with(client)
    def get(self, id):
        """
        Retrieves a list of clients for the given ticket
        """
        return Client.query.filter(Client.ticket_id == id).all()


@ns.route('/<int:id>/client/add')
@api.response(500, 'Client addition failed.')
class TicketClientAddition(Resource):

    @api.response(201, 'Client successfully added.')
    @api.expect(client)
    def post(self, id):
        """
        Creates a new client and adds it to the given ticket
        """
        data = request.json
        add_client(id, data)
        return 'Client successfully added.', 201


@ns.route('/<int:id>/garment')
@api.response(404, 'Ticket garments not found.')
class TicketGarmentCollection(Resource):

    @api.marshal_with(garment)
    def get(self, id):
        """
        Retrieves a list of garments for the given ticket
        """
        return Garment.query.filter(Garment.ticket_id == id).all()


@ns.route('/<int:id>/garment/add')
@api.response(500, 'Garment addition failed.')
class TicketGarmentAddition(Resource):

    @api.response(201, 'Garment successfully added.')
    @api.expect(garment)
    def post(self, id):
        """
        Creates a new garment and adds it to the given ticket
        """
        data = request.json
        add_garment(id, data)
        return 'Garment successfully added.', 201
