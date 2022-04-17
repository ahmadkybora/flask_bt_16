from flask import Blueprint
from app.Controllers.Panel.UserController import index, store, show, update, delete

UserRoute = Blueprint("UserRoute", __name__)

UserRoute.route('/', methods=['GET'])(index)
UserRoute.route('/create', methods=['POST'])(store)
UserRoute.route('/<int:user_id>', methods=['GET'])(show)
UserRoute.route('/<int:user_id>/edit', methods=['POST'])(update)
UserRoute.route('/<int:user_id>', methods=['DELETE'])(delete)