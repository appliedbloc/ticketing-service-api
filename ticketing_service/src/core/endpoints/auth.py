from flask import request
from flask_login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash
from flask_restplus import Resource

from ticketing_service import login_manager
from ticketing_service.database import db
from ticketing_service.database.models import User
from ticketing_service.src.core.utils.serializers import login_form, signup_form
from ticketing_service.src.restplus import api

# Blueprint Configuration
ns = api.namespace('auth', description='Authentication operations')


@ns.route('/login')
class LoginCollection(Resource):

    @api.response(201, 'User successfully logged in.')
    @api.expect(login_form)
    def post(self):
        """
        Logs in a user.
        """
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.check_password(password=password):
                return login_user(user)
        return 'Invalid username/password combination', 403


@ns.route('/signup', methods=['GET', 'POST'])
class SignupCollection(Resource):

    @api.response(201, 'User successfully signed up.')
    @api.expect(signup_form)
    def post(self):
        """
        Sign up a user.
        """
        data = request.json
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            user = User(name=name, username=username, password=generate_password_hash(password, method='sha256'),
                        email=email)
            db.session.add(user)
            db.session.commit()
            return login_user(user)
        return 'A user already exists with that email address.', 500


@ns.route("/logout")
class LogoutCollection(Resource):
    @login_required
    def get(self):
        """User log-out logic."""
        return logout_user()


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    print("AM I EVEN HERE?")
    print(user_id)
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return 'You must be logged in to view that page.', 401
