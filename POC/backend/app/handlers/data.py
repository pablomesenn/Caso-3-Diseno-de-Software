from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService
from app.services.data_service import DataService
from app.services.tripartite_service import TripartiteService
from app.utils.logging import log_request
from app.handlers.secure_data import token_required  # Added import

data_bp = Blueprint('data', __name__)
auth_service = AuthService()
data_service = DataService()
tripartite_service = TripartiteService()

@data_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    response, status = auth_service.login(email, password)
    log_request('/api/login', email or 'anonymous', 'success' if status == 200 else 'failed')
    return response, status

@data_bp.route('/query', methods=['POST'])
@token_required
def run_query():
    query = request.json.get('query')
    user_roles = request.user.get('groups', [])
    try:
        results = data_service.run_query(query, user_roles)
        log_request('/api/query', request.user.get('sub'), 'success')
        return jsonify({"results": results})
    except Exception as e:
        log_request('/api/query', request.user.get('sub'), 'failed')
        return jsonify({"message": f"Consulta fallida: {str(e)}"}), 500

@data_bp.route('/access-dataset/<dataset_id>', methods=['POST'])
@token_required
def access_dataset(dataset_id):
    shares = request.json.get('shares', [])
    try:
        secret = tripartite_service.reconstruct_secret(shares, dataset_id)
        log_request(f'/api/access-dataset/{dataset_id}', request.user.get('sub'), 'success')
        return jsonify({"message": f"Acceso concedido al dataset {dataset_id}", "secret": secret})
    except ValueError as e:
        log_request(f'/api/access-dataset/{dataset_id}', request.user.get('sub'), 'failed')
        return jsonify({"message": str(e)}), 403

@data_bp.route('/generate-shares/<dataset_id>', methods=['POST'])
@token_required
def generate_shares(dataset_id):
    secret = request.json.get('secret', 'default-secret')
    try:
        shares = tripartite_service.generate_key_shares(secret, dataset_id)
        log_request(f'/api/generate-shares/{dataset_id}', request.user.get('sub'), 'success')
        return jsonify({"shares": shares})
    except ValueError as e:
        log_request(f'/api/generate-shares/{dataset_id}', request.user.get('sub'), 'failed')
        return jsonify({"message": str(e)}), 500

@data_bp.route('/dashboard-url/<dataset_id>', methods=['GET'])
@token_required
def get_dashboard_url(dataset_id):
    try:
        # Simulate QuickSight dashboard URL
        embed_url = f"https://mock-quicksight.com/dashboards/{dataset_id}"
        log_request(f'/api/dashboard-url/{dataset_id}', request.user.get('sub'), 'success')
        return jsonify({"embedUrl": embed_url})
    except Exception as e:
        log_request(f'/api/dashboard-url/{dataset_id}', request.user.get('sub'), 'failed')
        return jsonify({"message": f"Error generando URL: {str(e)}"}), 500

@data_bp.route('/cost', methods=['GET'])
@token_required
def get_cost():
    try:
        # Simulate AWS cost data
        costs = [
            {"date": "2025-06-20", "cost": 100.50},
            {"date": "2025-06-21", "cost": 120.75}
        ]
        log_request('/api/cost', request.user.get('sub'), 'success')
        return jsonify({"costs": costs})
    except Exception as e:
        log_request('/api/cost', request.user.get('sub'), 'failed')
        return jsonify({"message": f"Error consultando costos: {str(e)}"}), 500