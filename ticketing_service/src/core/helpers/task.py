from ticketing_service.database import db
from ticketing_service.database.models import Task, Ticket


def add_task(ticket_id, data):
    task_type = data.get('task_type')
    assignee = data.get('assignee')
    sequence_order = data.get('sequence_order')

    ticket = Ticket.query.filter(Ticket.id == ticket_id).one()
    task = Task(task_type, assignee, sequence_order, ticket, ticket_id)

    db.session.add(task)
    db.session.commit()


def update_task(task_id, data):
    task = Task.query.filter(Task.id == task_id).one()
    task.task_type = data.get('title')
    task.assignee = data.get('body')
    task.sequence_order = data.get('sequence_order')

    ticket_id = data.get('ticket_id')
    task.ticket = Ticket.query.filter(Ticket.id == ticket_id).one()

    db.session.add(task)
    db.session.commit()

# def delete_task(task_id):
#     task = Task.query.filter(Task.id == task_id).one()
#     db.session.delete(task)
#     db.session.commit()
#
