import re
from flask import jsonify, request
from models.user_model import User

class UserController:

    @staticmethod
    def register_user(data):
        required_fields = ['first_name', 'last_name', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        role_id = 2  # Force regular user

        # Check for empty fields
        if not all([first_name.strip(), last_name.strip(), email.strip(), password.strip()]):
            return jsonify({'error': 'All fields are required'}), 400

        # Validate email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return jsonify({'error': 'Invalid email format'}), 400

        existing_user = User.get_user_by_email(email)
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 409

        try:
            new_user = User.create_user(first_name, last_name, email, password, role_id)
            return jsonify(new_user), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def login_user(data):
        if not all(k in data for k in ('email', 'password')):
            return jsonify({'error': 'Missing email or password'}), 400

        email = data['email']
        password = data['password']

        if not email.strip() or not password.strip():
            return jsonify({'error': 'Email and password are required'}), 400

        user = User.get_user_by_email(email)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        if user['password'] != password:
            return jsonify({'error': 'Incorrect password'}), 401

        return jsonify({'message': f'Welcome {user["first_name"]}'}), 200

    @staticmethod
    def get_all_users():
        try:
            users = User.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.get_user_by_id(user_id)
            if user:
                return jsonify(user), 200
            return jsonify({'error': 'User not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update_user(user_id):
        try:
            data = request.get_json()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            role_id = data.get('role_id')

            if not all([first_name, last_name, email, password, role_id]):
                return jsonify({'error': 'All fields are required.'}), 400

            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(email_pattern, email):
                return jsonify({'error': 'Invalid email format'}), 400

            result = User.update_user(user_id, first_name, last_name, email, password, role_id)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete_user(user_id):
        try:
            result = User.delete_user(user_id)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
