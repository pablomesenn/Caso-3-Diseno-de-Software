import os

JWT_SECRET = os.getenv('JWT_SECRET', 'super-secret-key')  # Use environment variable in production
ALGORITHMS = ['HS256']
MOCK_USERS = {
    'user1@example.com': {'password': 'password1', 'roles': ['User'], 'name': 'User One'},
    'admin@example.com': {'password': 'adminpass', 'roles': ['Admin'], 'name': 'Admin User'}
}
MOCK_DATASETS = {
    'dataset1': {'name': 'Dataset 1', 'accessible_to': ['Admin', 'User']},
    'dataset2': {'name': 'Dataset 2', 'accessible_to': ['Admin']}
}