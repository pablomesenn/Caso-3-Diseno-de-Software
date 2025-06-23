import pytest
from main import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('jwt.decode')
def test_secure_data_endpoint(mock_jwt, client):
    mock_jwt.return_value = {'sub': 'test_user', 'groups': ['User']}
    headers = {'Authorization': 'Bearer valid_token'}
    response = client.get('/api/secure-data', headers=headers)
    assert response.status_code == 200
    assert response.json == {"data": "Esto es información protegida por Okta"}

def test_secure_data_no_token(client):
    response = client.get('/api/secure-data')
    assert response.status_code == 401
    assert response.json['message'] == 'Token ausente o mal formado'