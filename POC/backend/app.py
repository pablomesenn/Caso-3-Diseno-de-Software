from flask import Flask, jsonify, request
import requests
from functools import wraps

app = Flask(__name__)

OKTA_ISSUER = 'https://dev-w425j2q1a431gpdw.us.okta.com/oauth2/default'
OKTA_AUDIENCE = 'api://default'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth or not auth.startswith('Bearer '):
            return jsonify({'message': 'Missing token'}), 401

        token = auth.split()[1]
        try:
            # Validación con introspection endpoint de Okta
            resp = requests.post(
                f'{OKTA_ISSUER}/v1/introspect',
                data={'token': token, 'token_type_hint': 'access_token'},
                auth=('AzrNIzpdapSkqzh4q1zUJRYZUX3KsXlD', 'a2kRzuJyTC9PfOs9tE_ivJlV304CLtUQSvKI4K3XIOUbzvTjgf5Dl9VzYqJymN_W'),
                headers={'Accept': 'application/json'}
            )
            token_data = resp.json()
            if not token_data.get('active'):
                return jsonify({'message': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'message': str(e)}), 401

        return f(*args, **kwargs)
    return decorated

@app.route("/api/secure-data", methods=["GET"])
@token_required
def secure_data():
    return jsonify({"data": "Esto es información protegida por Okta"})

if __name__ == "__main__":
    app.run(debug=True)
