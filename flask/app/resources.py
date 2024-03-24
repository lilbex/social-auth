from flask_restful import Resource
from flask import jsonify, request
from app import db
from .models import User


class HomePage(Resource):
    def get(self):
        return {'message': 'server is up and running'}, 200


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'error': 'User already exists'}), 400

        new_user = User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
