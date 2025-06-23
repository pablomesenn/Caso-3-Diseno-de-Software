from jwt import PyJWKClient
import jwt
from flask import jsonify
from app.config.config import OKTA_ISSUER, API_AUDIENCE, ALGORITHMS

class SecurityService:
    def __init__(self):
        self.jwks_client = PyJWKClient(f"{OKTA_ISSUER}/v1/keys")
        self.audience = API_AUDIENCE
        self.issuer = OKTA_ISSUER

    def validate_token(self, token):
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token).key
            decoded = jwt.decode(
                token,
                signing_key,
                algorithms=ALGORITHMS,
                audience=self.audience,
                issuer=self.issuer
            )
            return decoded, None, 200
        except jwt.ExpiredSignatureError:
            return None, jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError as e:
            return None, jsonify({'message': f'Token inválido: {str(e)}'}), 401