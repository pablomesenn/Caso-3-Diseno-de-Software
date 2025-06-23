import jwt
from flask import jsonify
from app.config.config import JWT_SECRET, ALGORITHMS, MOCK_USERS
from datetime import datetime, timedelta

class AuthService:
    def login(self, email, password):
        user = MOCK_USERS.get(email)
        if user and user['password'] == password:
            token = jwt.encode({
                'sub': email,
                'groups': user['roles'],
                'name': user['name'],
                'exp': datetime.utcnow() + timedelta(hours=1)
            }, JWT_SECRET, algorithm=ALGORITHMS[0])
            return jsonify({'token': token, 'name': user['name']}), 200
        return jsonify({'message': 'Credenciales inválidas'}), 401

    def validate_token(self, token):
        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=ALGORITHMS)
            return decoded, None, 200
        except jwt.ExpiredSignatureError:
            return None, jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError as e:
            return None, jsonify({'message': f'Token inválido: {str(e)}'}), 401