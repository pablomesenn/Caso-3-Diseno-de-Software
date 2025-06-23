from flask import Blueprint, jsonify, request
from app.security.auth import SecurityService
from app.security.tripartite import TripartiteKeyService
from app.services.data_service import DataService
from app.services.cost_service import CostService
from app.services.quicksight_service import QuickSightService
from main import log_request, token_required

data_bp = Blueprint('data', __name__)
security_service = SecurityService()
tripartite_service = TripartiteKeyService()
data_service = DataService()
cost_service = CostService()
quicksight_service = QuickSightService()

@data_bp.route('/access-dataset/<dataset_id>', methods=['POST'])
@token_required
def access_dataset(dataset_id):
    shares = request.json.get('shares', [])
    try:
        secret = tripartite_service.reconstruct_secret(shares)
        log_request(f'/api/access-dataset/{dataset_id}', request.user.get('sub'), 'success')
        return jsonify({"message": f"Access granted to dataset {dataset_id}"})
    except ValueError as e:
        log_request(f'/api/access-dataset/{dataset_id}', request.user.get('sub'), 'failed')
        return jsonify({"message": str(e)}), 403

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
        return jsonify({"message": f"Query failed: {str(e)}"}), 500

@data_bp.route('/cost', methods=['GET'])
@token_required
def get_cost():
    try:
        costs = cost_service.get_cost()
        log_request('/api/cost', request.user.get('sub'), 'success')
        return jsonify({"costs": costs})
    except Exception as e:
        log_request('/api/cost', request.user.get('sub'), 'failed')
        return jsonify({"message": f"Cost query failed: {str(e)}"}), 500

@data_bp.route('/dashboard-url/<dashboard_id>', methods=['GET'])
@token_required
def get_dashboard_url(dashboard_id):
    user_sub = request.user.get('sub')
    user_arn = f"arn:aws:iam::your_aws_account_id:user/{user_sub}"  # Replace with actual ARN logic
    try:
        embed_url = quicksight_service.generate_embed_url(user_arn, dashboard_id)
        log_request(f'/api/dashboard-url/{dashboard_id}', user_sub, 'success')
        return jsonify({"embedUrl": embed_url})
    except ValueError as e:
        log_request(f'/api/dashboard-url/{dashboard_id}', user_sub, 'failed')
        return jsonify({"message": str(e)}), 500