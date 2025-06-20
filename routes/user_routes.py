from flask import Blueprint, request
from controllers.user_controller import UserController

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    return UserController.register_user(data)

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    return UserController.login_user(data)

@auth_bp.route('/users', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@auth_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return UserController.get_user_by_id(user_id)

@auth_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return UserController.update_user(user_id)

@auth_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)