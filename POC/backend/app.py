from flask import Flask, jsonify, request
from flask_cors import CORS
import jwt
import requests
from jwt import PyJWKClient
from functools import wraps

app = Flask(__name__)
CORS(app)

AUTH0_DOMAIN = 'dev-w425j2q1a431gpdw.us.auth0.com'
API_AUDIENCE = 'api://default'
ALGORITHMS = ['RS256']

# Obtiene la clave pública para verificar los JWT
jwks_url = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'
jwks_client = PyJWKClient(jwks_url)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'message': 'Token ausente o mal formado'}), 401

        token = auth_header.split()[1]
        try:
            signing_key = jwks_client.get_signing_key_from_jwt(token).key
            decoded_token = jwt.decode(
                token,
                signing_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/'
            )
            # Aquí podrías usar `decoded_token` para identificar al usuario si quieres
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError as e:
            return jsonify({'message': f'Token inválido: {str(e)}'}), 401

        return f(*args, **kwargs)
    return decorated

@app.route("/api/secure-data", methods=["GET"])
@token_required
def secure_data():
    return jsonify({"data": "Esto es información protegida por Auth0"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
