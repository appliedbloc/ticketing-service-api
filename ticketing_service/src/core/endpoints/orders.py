from flask import request
from flask_restplus import Resource

from ticketing_service.src.core.helpers.client import *
from ticketing_service.src.core.helpers.order import *
from ticketing_service.src.core.helpers.ticket import *
from ticketing_service.src.core.utils.serializers import client, order, order_detailed, ticket
from ticketing_service.src.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('orders', description='CRUD order operations')


@ns.route('/')
class OrderCollection(Resource):

    @api.marshal_list_with(order)
    def get(self):
        """
        Returns list of orders.
        """
        log.info('Listing all orders')

        orders = Order.query.all()
        return orders

    @api.response(201, 'Order successfully created.')
    @api.expect(order)
    def post(self):
        """
        Creates a new order.
        """
        data = request.json
        create_order(data)
        return 'Order successfully created.', 201


@ns.route('/<int:id>')
@api.response(404, 'Order not found.')
class OrderItem(Resource):

    @api.marshal_with(order_detailed)
    def get(self, id):
        """
        Returns a single order with a given id.
        """
        log.info('Looking up order')

        return Order.query.filter(Order.id == id).one()

    @api.expect(order)
    @api.response(204, 'Order successfully updated.')
    def put(self, id):
        """
        Updates an order with a given id.
        """
        data = request.json
        update_order(id, data)
        return None, 204

    @api.response(204, 'Order successfully deleted.')
    def delete(self, id):
        """
        Deletes an order with a given id.
        """
        delete_order(id)
        return None, 204


@ns.route('/<int:id>/tickets')
@api.response(404, 'Ticket tasks not found.')
class OrderTicketsCollection(Resource):

    @api.marshal_with(ticket)
    def get(self, id):
        """
        Retrieves list of tickets for the order with a given id
        """
        log.info('Looking up tickets for an order')

        return Ticket.query.filter(Ticket.order_id == id).all()


@ns.route('/<int:id>/tickets/add')
@api.response(500, 'Ticket addition failed.')
class OrderTicketsAddition(Resource):

    @api.response(201, 'Ticket successfully added.')
    @api.expect(ticket)
    def post(self, id):
        """
        Creates a new ticket and adds it to the order with a given id
        """
        data = request.json
        add_ticket(id, data)
        return 'Ticket successfully added.', 201


@ns.route('/<int:id>/client')
@api.response(404, 'Order client not found.')
class OrderClientCollection(Resource):

    @api.marshal_with(client)
    def get(self, id):
        """
        Retrieves a list of clients for the order with a given id
        """
        return Client.query.filter(Client.order_id == id).all()


@ns.route('/<int:id>/client/add')
@api.response(500, 'Client addition failed.')
class OrderClientAddition(Resource):

    @api.response(201, 'Client successfully added.')
    @api.expect(client)
    def post(self, id):
        """
        Creates a new client and adds it to the order with a given id
        """
        data = request.json
        add_client(id, data)
        return 'Client successfully added.', 201
