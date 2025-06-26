from flask import Blueprint, jsonify, request
from functools import wraps
from app.services.auth_service import AuthService
from app.utils.logging import log_request

secure_data_bp = Blueprint('secure_data', __name__)
auth_service = AuthService()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or not auth_header.startswith('Bearer '):
            log_request(request.path, 'anonymous', 'failed')
            return jsonify({'message': 'Token ausente o mal formado'}), 401
        token = auth_header.split()[1]
        decoded, error, status = auth_service.validate_token(token)
        if error:
            log_request(request.path, 'anonymous', 'failed')
            return error, status
        request.user = decoded
        return f(*args, **kwargs)
    return decorated

@secure_data_bp.route('/secure-data', methods=['GET'])
@token_required
def secure_data():
    log_request('/api/secure-data', request.user.get('sub'), 'success')
    return jsonify({"data": "Esto es información protegida"})